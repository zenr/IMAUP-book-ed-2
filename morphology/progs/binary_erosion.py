from PIL import Image
import scipy.ndimage as snd
import numpy as np
import cv2

# Opening the image and converting it to grayscale.
a = Image.open('../figures/er_image.png').convert('L')
a = np.array(a)
# Performing binary erosion for 20 iterations.
b = snd.morphology.binary_erosion(a,iterations=20)
# Saving the image as 8-bit as b is a
# binary image of dtype=bool
cv2.imwrite('../figures/er_binary_output_20.png', b*255)
