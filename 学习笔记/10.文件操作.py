# 1.文件读取 r:read w:write a:append t:text b:byte
import csv

# data = open(file='../data.csv',mode='r',encoding='utf-8')
# print(data)
# content = data.read()
# print(content)
# data.close()

# 如果文件不存在会报错,方法1try
content = None
try:
    f = open(file='./game.txt',mode='r',encoding='utf-8')
    content = f.read()
except:
    print('文件不存在!')
finally:
    print(content)
# 方法2 with
with open('./game.txt',mode='r',encoding='utf-8') as f:
    content = f.read()
    print(content)

# 2.文件写入
data1 = '小乔要努力变强!'
game = (open(file='./game.txt',mode='w',encoding='utf-8'))
game.write(data1)
print(game)
game.close()

data2 = ['周瑜大人!','这是谁家的小狗!','花会枯萎,爱永不凋零']
game1 = open(file='./game.txt',mode='a',encoding='utf-8')
for i in data2:
    game1.write(i+'\n')
game1.close()
# 3.csv文件的写入
import csv
data3 = [['周瑜大人!','1'],['这是谁家的小狗!','2'],['花会枯萎,爱永不凋零','3']]
with open(file='./game1.csv',mode='w',encoding='utf-8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['台词1','表头'])  #添加表头
    # for i in data3:
    #     writer.writerow(i)
    writer.writerows(data3) #更简单的方式多行写入
# 4.csv文件的读取
with open(file='./game1.csv',mode='r',encoding='utf-8',newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)