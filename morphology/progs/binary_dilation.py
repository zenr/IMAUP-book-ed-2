from PIL import Image
import scipy.ndimage as snd
import numpy as np
import cv2

# Opening the image and converting it to grayscale.
a = Image.open('../figures/dil_image.png').convert('L')
a = np.array(a)
# Performing binary dilation for 5 iterations.
b = snd.morphology.binary_dilation(a, iterations=5)
# Saving the image as 8-bit as b is a
# binary image of dtype=bool
cv2.imwrite('../figures/di_binary.png', b*255)
