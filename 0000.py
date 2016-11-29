# _*_  coding:utf-8 _*_
from PIL import Image, ImageDraw, ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('Arial.ttf',size = 80)
    fillcolor = "#ff0000"
    width,height = img.size
    draw.text((width-40,0),'9', font = myfont, fill=fillcolor)
    image.save('result.jpg','jpeg')
    
    return 0

if __name__=='__main__':
    image = Image.open('0000.jpg')
    add_num(image)