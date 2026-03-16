animal = ['库洛米','大耳兔','玉桂狗']
print(animal[1])
print(animal[:2])
print(animal[:])
# 计算列表长度
print(len(animal))

# 增加元素
animal.append('嘉儿')
print(animal)
# 删除元素
animal.pop() # 删除最后一个元素
print(animal)
animal.pop(0) #加索引删除
print(animal)

animal.remove(animal[0])
print(animal)
# 替换
animal[0] = '佩奇'
print(animal)
# 插入
animal.insert(1,'乔治')
print(animal)
# 查询
n = animal.index('乔治')
print(n)
print('大乔' not in animal)
# 统计
animal.append('乔治')
animal.append('乔治')
print(animal.count('乔治'))
