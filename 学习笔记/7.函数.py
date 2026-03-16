def login(): #定义函数
    username = input('输入用户名:')
    password = input('输入密码:')
    if username == 'admin' and password == '1234':
        print('登录成功')
    else:
        print('登录失败')
login() #调用函数
def love(choice): #有形参
    hero= {1:'大乔',2:"小乔",3:'王昭君'}
    if choice in hero.keys():
        print('你喜欢的英雄是{}'.format(hero[choice]))
    else:
        print('你喜欢的英雄我们没有')
love(1) #调用时叫实参
love(2)