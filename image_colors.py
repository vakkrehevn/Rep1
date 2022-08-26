import json
from PIL import Image


class ImageColors:
    def recognize_color(self, draw_map2, exept=None):
        input_image = Image.open('jelly.png')
        pixel_map = ''
        width, height = input_image.size
        for j in range(height):
            for i in range(width):
                r, g, b, p = input_image.getpixel((i, j))
                try:
                    if draw_map2[(r, g, b, 255)] == 0:
                        pixel_map+="0 "
                    else:
                        pixel_map+="-1 "
                except:
                    pixel_map+="0 "
            pixel_map+="\n"

        with open('image_resource.txt', 'w') as outfile:
            outfile.write(pixel_map)
#
