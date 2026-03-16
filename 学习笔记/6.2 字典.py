love = {'姓名':'库洛米','颜色':'紫色','种族':'精灵'}
print(love.keys())
print(love.values())
# 查询
print(love['姓名'])
print(love.get('特点','未知'))
# 添加
love['特点'] = '可爱' #键不存在是添加
print(love)
# 修改
love['特点'] = '精灵古怪' #键存在是修改
print(love)
# 删除
love.pop('姓名')
print(love)
# 查询键是否存在
print('种族' in love)
# 查询值是否存在
print('库洛米' in love.values())