from PIL import Image, ImageTk

image = Image.open('logo.png')

size = image.size

width = size[0]
height = size[1]
print(width)
print(height)