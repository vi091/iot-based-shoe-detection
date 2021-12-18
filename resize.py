from PIL import Image
import os

files = os.listdir('./images')
for file in files:
    im = Image.open('./images/' + file)
    newsize = (3120, 3120)
    im1 = im.resize(newsize)
    im1.save('./updated_images/' + file)
