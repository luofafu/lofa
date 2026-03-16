# while循环
i = 1
number = int(input("请输入你想要循环的次数:"))
while i <= number:
    print('开始')
    i += 1
    if number > 4:
        print("最多4次循环")
        break
# for循环
for i in range(3):
    username = input('请输入用户名:')
    password = input('请输入密码:')
    if username == 'admin' and password == '123456':
        print('登录成功!')
        break
    else:
        print('登录失败,剩余{}次机会'.format(3-i-1))