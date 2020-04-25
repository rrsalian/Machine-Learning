""" import cv
im = cv.imread("image.jpg", mode='RGB')
print(type(im)) """

# load and show an image with Pillow
from PIL import Image
# Open the image form working directory
image = Image.open('image.jpg')
# summarize some details about the image
print(image.format)
print(image.size)
print(image.mode)
# show the image
load_image.show()
