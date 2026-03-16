# if
money = input("请输入你的金额:")
money = float(money)
number  = input("请输入你需要几个礼物?(20元/个):")
number = int(number)
name = input("请输入你想要的礼物名字:")
if money >= 20*number and name == '库洛米':
    print("你有{}可以买{}个{},找你{}零钱".format(money,number,name,money-20*number))
# if嵌套语句
color = input('请输入健康码颜色:1.绿色 2.红色 3.黄色')
if color == '1':
    print("请测量体温")
    temperate = float(input('请输入体温:'))
    if temperate <= 37.5:
        print('体温正常可以进入!')
    else:
        print('体温异常不能进入!')
else:
    print('抱歉你需要进行隔离!')