import numpy as np
from PIL import Image
from skimage.morphology import skeletonize
import cv2

# Opening the image and converting it to grayscale.
a = Image.open('../figures//steps1.png').convert('L')
# Converting a to an ndarray and normalizing it.
a = np.asarray(a)/np.max(a)
# Performing skeletonization.
b = skeletonize(a)
# Saving the image as 8-bit as b is a
# binary image of dtype=bool
cv2.imwrite('../figures/skeleton_output.png', b*255)
