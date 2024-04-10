import cv2
import os
from PIL import Image

#pillow = image processing library

path = "images"
meanwidth = 0
meanheight = 0
files = os.listdir(path)
print(files)
num_of_images = len(files)
print(num_of_images)

for file in files:
    image = Image.open(os.path.join(path,file))
    width,height = image.size
    print(image.size)
    meanwidth = meanwidth + width
    meanheight = meanheight + height

meanwidth = meanwidth//num_of_images
meanheight = meanheight//num_of_images
print(meanheight)
print(meanwidth)

for file in files:
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
        image = Image.open(os.path.join(path,file))
        imageresized = image.resize((meanwidth,meanheight), Image.ANTIALIAS)
        imageresized.save(file, "JPEG", quality = 95)

