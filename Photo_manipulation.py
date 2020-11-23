from PIL import Image
import os
import math

images_path = ('PATH')
size = 300*300
destination_path = (images_path + '\\modified_images')  # The destination where the modified files will be saved.

try:
    os.mkdir(destination_path)
except FileExistsError:
    pass

# This for loop takes a directory with images, rotates them to be all vertical and resizes according to desired size
# while maintaining the same width/height ratio
image_count = 1
for file in os.listdir(images_path):
    if os.path.isdir(images_path + '\\' + file):
        continue
    else:
        image = Image.open(images_path + '\\' + file)
        width, height = image.size
        area = width * height
        ratio = math.sqrt(size/area)
        new_width = int(round(width * ratio))
        new_height = int(round(height * ratio))
        image = image.resize((new_width, new_height))
        if width > height:
            image = image.rotate(90)
        image.save('{}/image{}.jpg'.format(destination_path, str(image_count)))
        image_count += 1
