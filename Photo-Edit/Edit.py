from PIL import Image, ImageEnhance, ImageFilter
import os

path = './pics'
pathOut = '/editedpics'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    edit = img.filter(ImageFilter.SHARPEN)

    clean_name = os.path.splitext(filename)[0]
    factor=1.5
    fact2= 1.2
    enhancer = ImageEnhance.Contrast(edit)
    

    edit = enhancer.enhance(factor)
    enhancer2 = ImageEnhance.Brightness(edit)
    edit = enhancer.enhance(fact2)


    edit.save(f'.{pathOut}/{clean_name}_edited3.jpg')
