# class 类名: 类名首字母大写
#     属性
#     方法
class Phone:
    color = '黑色'
    type = 'Mete30'
    price = 3999

    def __init__(self, brand):  # 构造函数
        print(self)
        self.brand = brand

    def call(self, name):
        if name == 'lofa':
            print('使用' + self.brand + '打电话')
    def send_message(self):
        print('可以发信息')


phone = Phone('小米')
print(phone)
print(phone.brand)  # 调用属性
print(phone.price)
phone.call(name='lofa')  # 调用方法
# 修改对象属性
print(phone.brand)
phone.brand = '小米'  # 动态添加
print(phone.brand)
# 类的继承
class Shouji(Phone):
    def kind(self):
        print(self.brand+'就是好')
SJ = Shouji('小米')
SJ.kind()