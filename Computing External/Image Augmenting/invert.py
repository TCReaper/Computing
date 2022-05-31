import numpy as np
import cv2 as cv

# def Inversion(Image):
#     height = Image.shape[0]
#     width = Image.shape[1]
#     channels = Image.shape[2]

#     size = ( height , width , channels )
#     new = np.zeros( size , np.uint8 )
#     for x in range(height):
#         for y in range(width):
#             for c in range(channels):
#                 new[x,y,c] = 255 - Image[x,y,c]
#     return new

from PIL import Image
import colorsys

# rgb_to_hsv = np.vectorize(colorsys.rgb_to_hsv)
# hsv_to_rgb = np.vectorize(colorsys.hsv_to_rgb)

# def shift_hue(arr, hout):
#     r, g, b, a = np.rollaxis(arr, axis=-1)
#     h, s, v = rgb_to_hsv(r, g, b)
#     h = hout
#     r, g, b = hsv_to_rgb(h, s, v)
#     arr = np.dstack((r, g, b, a))
#     return arr

# def colorize(image, hue):
#     """
#     Colorize PIL image `original` with the given
#     `hue` (hue within 0-360); returns another PIL image.
#     """
#     img = image.convert('RGBA')
#     arr = np.array(np.asarray(img).astype('float'))
#     new_img = Image.fromarray(shift_hue(arr, hue/360.).astype('uint8'), 'RGBA')

#     return new_img



path = r'C:\Users\haosh\Documents\GitHub\Computing\Computing External\Image Augmenting\images\original.jpg'

img = cv.imread(path)

# inverted = Inversion(img)
# cv.imwrite("Inverted.png",inverted)

# shifted = colorize(img,180)
# cv.imwrite("shifted.png",shifted)

