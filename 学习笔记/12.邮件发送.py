from datetime import time
from time import sleep

import schedule
import yagmail
def task():
    # yag = yagmail.register('3023723263@qq.com','axwbmukzwyadddga')  #登录邮箱
    yag = yagmail.SMTP(user = '3023723263@qq.com',host = 'smtp.qq.com')
    # 携带附件
    obj = yagmail.inline('E:\\公考\\信息\\论文\\202010430115_罗发富\\202010430115_罗发富\\8. 毕业论文初稿、定稿（查重稿）、最终稿\\202010430115_罗发富_基于大数据架构的电商平台的设计与实现（最终版）.docx')
    contents  = ['<h1>Hello Pluto</h1>','<b>这是一封邮件</b>','<a href='"https://www.cnblogs.com/Pluto-Love-Learn"'>你收到了吗？</a>',obj]

    yag.send('3023723263@qq.com','Python',contents = contents)


def task1():
    # yag = yagmail.register('3023723263@qq.com','axwbmukzwyadddga')  #登录邮箱
    yag = yagmail.SMTP(user = '3023723263@qq.com',host = 'smtp.qq.com')
    contents  = ['<h1>你好 Pluto!</h1>']
    yag.send(['3023723263@qq.com','2001@qq.com'],'Pyton群发文件',contents = contents)

def task():
    # yag = yagmail.register('3023723263@qq.com','axwbmukzwyadddga')  #登录邮箱
    yag = yagmail.SMTP(user = '3023723263@qq.com',host = 'smtp.qq.com')
    # 携带附件(图片、表格、文件等)
    obj = yagmail.inline('E:\\公考\\信息\\论文\\202010430115_罗发富\\202010430115_罗发富\\8. 毕业论文初稿、定稿（查重稿）、最终稿\\202010430115_罗发富_基于大数据架构的电商平台的设计与实现（最终版）.docx')
    contents  = ['<h1>Hello Pluto</h1>','<b>这是一封邮件</b>','<a href='"https://www.cnblogs.com/Pluto-Love-Learn"'>你收到了吗？</a>',obj]

    yag.send('3023723263@qq.com','Python',contents = contents)
schedule.every(10).minutes.do(task) #部署每10分钟执行一次task函数任务
# schedule.every().hour.do(task) #部署每*小时执行一次task函数任务
# schedule.every().day.at("10:30").do(task) #部署每天10.30执行一次task函数任务
# schedule.every().sunday.do(task) #部署每个星期日执行一次task函数任务
# schedule.every().friday.at("12.00").do(task) #部署每个星期五的12.00执行一次task函数任务

while True:
    schedule.run_pending()
    sleep(1)