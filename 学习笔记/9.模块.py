from package.create_module import *
from package.magic import use_magic
print(name)

import package.create_module as cm
c = cm.Course('生物课')
print(c.name)

use_magic() #调用函数