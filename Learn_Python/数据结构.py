# 01.列表[] 可变容器
list = [1,2,3,4,5]
list.append(6) # 末尾添加
list.insert(1,'1') #指定插入
list.remove('1') #删除
list.pop(0) #指定删除
del list[0] # 性能占优
# list.clear() #清除
print(list.index(3)) #查询
print(list.count(5)) #统计
list.sort() #排序
list.reverse()
# list = [i for i in list if i >1] 列表生成式

# 02.元祖() 不可变类型
tuple = (1,2,3,4,5)
print(len(tuple)) #查看元祖数量
a = 1,20,100 #打包
b,c,*d = a #解包

# 03.字符串'' 不可变类型
str = 'hello world'
print(str.find('o',1)) #从第二个开始查找
print(str.index('o',0))
#格式化
a = 3
b = 1
print('%d * %d = %d' % (a,b,a*b))
print('{0} * {1} = {2}'.format(a,b,a*b))
print(f'{a} * {b} = {a*b}')
str1 = '！lofa！'
print(str1.strip()) #去除头尾空格
print(str1.lstrip('！')) #去除头
print(str1.rstrip('！')) #去除尾
print(str1.replace('lo','Lo')) #替换
str2 = 'Pluto Lofa'
print(str2.split()) #拆分
print('-'.join(str2.split())) #合并
a = str2.encode('utf-8') #编码
a.decode('utf-8') #解码

# 04.集合{} 可变 不重复 无序 性能优于列表的成员运算
# 可变类型不能放进集合 如:列表
set = {num for num in range(20) if num % 3 == 0 or num % 7 ==0}
for set1 in set:
    print(set1)
print(9 in set) #成员运算
print(10 not in set)
print('---------------------------------')
# 二元运算
set1 = {1,2,3,4,5,6}
set2 = {2,4,5,6,8}
print(set1 & set2) #交集
print(set1.intersection(set2))
print(set1 | set2) #并集
print(set1.union(set2))
print(set1 - set2) #差集
print(set1.difference(set2))
print(set1 ^ set2) #对称差
print(set1.symmetric_difference(set2))
set.add(10) #添加
set.discard(10) #删除
if 10 in set:
    set.remove(10)
print(set)
set.clear() #清空
set1.isdisjoint(set2) #判断是否存在相同元素,不存在:True
fset = frozenset({1,3,5}) #不可变集合

# 05.字典 可变 dictionary {:} 键为不可变类型
person = dict(name = 'lofa',age = 18,height = 175 ,weight = 160)
item = dict(zip('ABCD','1234')) #压缩两个序列创建字典
item1 = {x :x**3 for x in  range(10)} #字典生成式
print(item1)
for key in person:
    print(f'{key}:\t{person[key]}')
print('name' in person)
print(person['name'])
person['love'] = '小乔' #索引添加
print(person.get('love')) #没有键返回None
person.keys() #获取所有键
person.values() #获取所有值
person.items() #获取键值
for key,value in  person.items():
    print(f'{key}:\t{value}')
person.update(item) #person有更新,没有就添加
person |= item
person.pop('age')
person.popitem() #删除尾
person.clear() #清除
print(person)
