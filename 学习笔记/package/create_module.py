name = 'Harry Potter '
age = 18

def fight(tool=None):
    if tool:
        print('在魔法学院驾驶'+ tool + '练习飞行课')
    else:
        print('走到魔法学院就会练习飞行课')

class Course:
    def __init__(self,name,c_list=[]):
        self.name = name
        self.c_list = []
    def add_course(self,c_name):
        if c_name:
            self.c_list.append(c_name)
        else:
            print('选修课不能为空！')
    def remove_course(self,c_name):
        if c_name:
            self.c_list.remove(c_name)
        else:
            print('选修课不能为空')