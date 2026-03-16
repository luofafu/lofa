# ''  ""  ''''''
message = "花会枯萎,爱永不凋零!"
print(message[0])
print(message[0:4])
# 查询
print(message.find('小乔')) #不在会返回-1
print(message.index('枯萎')) #不在会报错
# 开头结尾查询
print(message.startswith('花'))
print(message.endswith('凋零!'))
# 去除空白字符
a = '     小乔要努力变强 \t  周瑜  大人    ' #字符串中间的空白字符不能去掉
print(a)
print(a.strip())