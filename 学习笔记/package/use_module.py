# import create_module
# import create_module as cm #减少代码

from create_module import name,Course
from create_module import *

# 第一种方法
# print(create_module.name)
# create_module.fight()
# c = create_module.Course('哈利')
# c.add_course('黑魔法防御术')
# print(c.name)
# print(c.c_list)

# 第二种方法
# print(cm.name)
# cm.fight()
# c = cm.Course('哈利')
# c.add_course('黑魔法防御术')
# print(c.name)
# print(c.c_list)

# 第三种方法
def use_magic():
    print('我会施展厉害的魔法')
print(name)