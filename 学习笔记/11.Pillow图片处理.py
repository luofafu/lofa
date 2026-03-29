import PIL
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

image = Image.open(fp='魔女.jpg')
# image.show() #展示图片
print(image.size)  #图片大小
print(image.mode) #图片模式
print(image.format) #图片格式
image1 = image.convert('L')

# 修改图片
image2 = Image.new('RGB',(220,150),(20,112,255))
# image2.show()
def get_color():
     red = random.randint(0, 255)
     green = random.randint(0, 255)
     blue = random.randint(0, 255)
     return (red, green, blue)
def get_code(length):
     s = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
     code = ''
     for i in range(length):
         code += random.choice(s)
     return code

def draw_code():
     # 定义话不的长度和宽度
     width = 120
     height = 120
     image_size = (width,height)

     #定义画布
     image = Image.new('RGB', image_size,get_color())
     #定义画笔
     draw = PIL.ImageDraw.Draw(image)
     #产生验证码
     code = get_code(4)
     myfont = PIL.ImageFont.truetype(font='C:/Windows/Fonts/Arial.ttf', size=30)
     #逐个绘制
     for i in range(4):
         distance_x = random.randint(30*i,30*i+5)
         distance_y = random.randint(0,5)
         draw.text((distance_x,distance_y),code[i],font =myfont,fill =get_color())

     image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
     image.show()
draw_code()



