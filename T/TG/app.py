from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
import requests
import json
import time
import hashlib

# 加载环境变量
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'sqlite:///shop.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 数据库初始化
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# 商品模型
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

# 订单模型
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product = db.relationship('Product', backref=db.backref('orders', lazy=True))
    amount = db.Column(db.Float, nullable=False)
    order_no = db.Column(db.String(32), nullable=False, unique=True)
    status = db.Column(db.String(20), nullable=False, default='pending')
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

# 微信支付配置
WECHAT_APPID = os.environ.get('WECHAT_APPID', 'your-appid')
WECHAT_MCHID = os.environ.get('WECHAT_MCHID', 'your-mchid')
WECHAT_API_KEY = os.environ.get('WECHAT_API_KEY', 'your-api-key')
WECHAT_NOTIFY_URL = os.environ.get('WECHAT_NOTIFY_URL', 'http://your-domain.com/wechat/notify')

# 首页 - 商品列表
@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

# 商品详情页
@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)

# 生成订单
@app.route('/create_order/<int:product_id>', methods=['POST'])
def create_order(product_id):
    product = Product.query.get_or_404(product_id)
    
    # 生成订单号
    order_no = str(int(time.time() * 1000)) + str(product_id)
    
    # 创建订单
    order = Order(
        product_id=product.id,
        amount=product.price,
        order_no=order_no,
        status='pending'
    )
    
    try:
        db.session.add(order)
        db.session.commit()
        
        # 跳转到微信支付
        return redirect(url_for('wechat_pay', order_id=order.id))
    except Exception as e:
        db.session.rollback()
        flash('创建订单失败，请重试', 'error')
        return redirect(url_for('product_detail', product_id=product_id))

# 微信支付页面
@app.route('/wechat/pay/<int:order_id>')
def wechat_pay(order_id):
    order = Order.query.get_or_404(order_id)
    
    # 构建微信支付参数
    nonce_str = hashlib.md5(str(time.time()).encode()).hexdigest()
    body = order.product.name
    total_fee = int(order.amount * 100)  # 单位：分
    out_trade_no = order.order_no
    spbill_create_ip = request.remote_addr
    notify_url = WECHAT_NOTIFY_URL
    trade_type = 'NATIVE'
    
    # 构建签名
    params = {
        'appid': WECHAT_APPID,
        'mch_id': WECHAT_MCHID,
        'nonce_str': nonce_str,
        'body': body,
        'total_fee': total_fee,
        'out_trade_no': out_trade_no,
        'spbill_create_ip': spbill_create_ip,
        'notify_url': notify_url,
        'trade_type': trade_type
    }
    
    # 按照字母顺序排序
    sorted_params = sorted(params.items(), key=lambda x: x[0])
    sign_str = '&'.join([f'{k}={v}' for k, v in sorted_params])
    sign_str += f'&key={WECHAT_API_KEY}'
    
    # 计算签名
    sign = hashlib.md5(sign_str.encode()).hexdigest().upper()
    params['sign'] = sign
    
    # 构建XML
    xml_data = '<xml>'
    for k, v in params.items():
        xml_data += f'<{k}>{v}</{k}>'
    xml_data += '</xml>'
    
    # 调用微信支付API
    url = 'https://api.mch.weixin.qq.com/pay/unifiedorder'
    try:
        response = requests.post(url, data=xml_data.encode('utf-8'), headers={'Content-Type': 'application/xml'})
        response.encoding = 'utf-8'
        
        # 解析XML响应
        from xml.etree import ElementTree as ET
        root = ET.fromstring(response.text)
        
        if root.find('return_code').text == 'SUCCESS' and root.find('result_code').text == 'SUCCESS':
            code_url = root.find('code_url').text
            return render_template('wechat_pay.html', order=order, code_url=code_url)
        else:
            error_msg = root.find('return_msg').text
            flash(f'微信支付调用失败: {error_msg}', 'error')
            return redirect(url_for('product_detail', product_id=order.product.id))
    except Exception as e:
        flash(f'微信支付调用失败: {str(e)}', 'error')
        return redirect(url_for('product_detail', product_id=order.product.id))

# 微信支付回调
@app.route('/wechat/notify', methods=['POST'])
def wechat_notify():
    try:
        # 解析XML
        from xml.etree import ElementTree as ET
        root = ET.fromstring(request.data)
        
        # 验证签名
        params = {}
        for child in root:
            if child.tag != 'sign':
                params[child.tag] = child.text
        
        # 构建签名
        sorted_params = sorted(params.items(), key=lambda x: x[0])
        sign_str = '&'.join([f'{k}={v}' for k, v in sorted_params])
        sign_str += f'&key={WECHAT_API_KEY}'
        
        # 计算签名
        sign = hashlib.md5(sign_str.encode()).hexdigest().upper()
        
        if sign == root.find('sign').text and root.find('return_code').text == 'SUCCESS':
            # 更新订单状态
            order_no = root.find('out_trade_no').text
            order = Order.query.filter_by(order_no=order_no).first()
            if order:
                order.status = 'paid'
                db.session.commit()
            
            # 返回成功响应
            return '<xml><return_code><![CDATA[SUCCESS]]></return_code><return_msg><![CDATA[OK]]></return_msg></xml>'
        else:
            return '<xml><return_code><![CDATA[FAIL]]></return_code><return_msg><![CDATA[签名失败]]></return_msg></xml>'
    except Exception as e:
        return '<xml><return_code><![CDATA[FAIL]]></return_code><return_msg><![CDATA[处理失败]]></return_msg></xml>'

# 支付成功页面
@app.route('/payment/success/<int:order_id>')
def payment_success(order_id):
    order = Order.query.get_or_404(order_id)
    if order.status != 'paid':
        flash('订单尚未支付', 'error')
        return redirect(url_for('product_detail', product_id=order.product.id))
    
    return render_template('payment_success.html', order=order)

# 检查支付状态 API
@app.route('/check_payment/<int:order_id>')
def check_payment(order_id):
    order = Order.query.get_or_404(order_id)
    return {
        'order_id': order.id,
        'status': order.status,
        'amount': order.amount
    }

# 测试数据初始化
@app.cli.command('init_data')
def init_data():
    # 创建测试商品
    products = [
        Product(
            name='iPhone 15 Pro',
            price=7999.00,
            description='全新iPhone 15 Pro，搭载A17 Pro芯片，钛金属机身',
            image_url='https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=iPhone%2015%20Pro%20titanium%20smartphone%20product%20photo&image_size=square'
        ),
        Product(
            name='MacBook Pro 14',
            price=16999.00,
            description='M3 Pro芯片，14英寸Liquid Retina XDR显示屏',
            image_url='https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=MacBook%20Pro%2014%20inch%20laptop%20product%20photo&image_size=square'
        ),
        Product(
            name='AirPods Pro 2',
            price=1899.00,
            description='主动降噪，空间音频，MagSafe充电盒',
            image_url='https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=AirPods%20Pro%202%20wireless%20earbuds%20product%20photo&image_size=square'
        )
    ]
    
    for product in products:
        if not Product.query.filter_by(name=product.name).first():
            db.session.add(product)
    
    db.session.commit()
    print('测试数据初始化完成')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)