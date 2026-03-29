# 函数 /:强制位置参数 *:命名关键字参数
def demo(a,b,/):
    return a + b
print(demo(1,2,))
def demo2(*,a,b):
    return a + b
print(demo2(a=1,b=2))
def demo3(b,a=1): #a默认值为1
    return a + b
print(demo3(b=2,a=3))
def demo4(*a,b): #表示可变参数:将传入的参数封转进元组
    print(a,b)
print(demo4(2,b =3))
def demo5(*b,**a): #表示可变关键字参数:将传入参数封装进字典
    print(a)
    print(b)
    return a
print(demo5(2,3,4,name='lofa'))