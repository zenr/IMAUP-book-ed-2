from PIL import Image
import scipy.ndimage as snd
import numpy as np
import cv2

# Opening the image and converting it to .
a = Image.open('../figures/dil_image.png').convert('L')
a = np.array(a)
# Defining the structuring element.
s = [[0,1,0],[1,1,1], [0,1,0]]
# Performing the binary opening for 5 iterations.
b = snd.morphology.binary_opening(a, structure=s, iterations=5)
# Saving the image as 8-bit as b is a
# binary image of dtype=bool
cv2.imwrite('../figures/opening_binary.png', b*255)
