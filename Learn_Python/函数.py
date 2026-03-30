# 函数 /:强制位置参数 *:命名关键字参数
def demo(a,b,/):
    return a + b
def demo2(*,a,b):
    return a + b
demo2(a=1,b=2)
def demo3(b,a=1): #a默认值为1
    return a + b
def demo4(*a,b): #表示可变参数:将传入的参数封转进元组
    print(a,b)
demo4(2,b =3)
def demo5(*b,**a): #表示可变关键字参数:将传入参数封装进字典
    print(a)
    print(b)
    return a
demo5(2,3,4,name='lofa')

# lambda 参数:表达式 lambda匿名函数
# 修饰器
import random
import time

def record_time(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间: {end - start:.2f}秒')
        return result

    return wrapper

@record_time
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')


@record_time
def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')

download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')
'''
开始下载MySQL从删库到跑路.avi.
MySQL从删库到跑路.avi下载完成.
download执行时间: 3.00秒
开始上传Python从入门到住院.pdf.
Python从入门到住院.pdf上传完成.
upload执行时间: 1.62秒
'''