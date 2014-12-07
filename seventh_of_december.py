__author__ = 'martinsolheim'


from PIL import Image
from collections import defaultdict
import os

path_dir = os.path.dirname(__file__)
filename = os.path.join(path_dir, "data/santa.png")

im = Image.open(filename)
pixels = im.load()

width, height = im.size

pixel_dict = defaultdict(int)
for x in range(width):
    for y in range(height):
        pixel = pixels[x, y]
        pixel_dict[pixel] += 1

pixel_values = []
for value in pixel_dict.values():
    pixel_values.append(value)

pixel_values.sort(reverse=True)

print(pixel_values[9])
