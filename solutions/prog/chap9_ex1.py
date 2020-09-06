import numpy as np
from skimage.morphology import skeletonize
import scipy
import cv2

# opening the image and converting it to a greyscale image
a = cv2.imread('figure/dil_image1.png')
a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)

# converting a to an ndarray and normalizing it
a = a/np.max(a)
# performing skeletonization
b = skeletonize(a)

# b is a binary image, we can convert it to gray scale
# by multiplying by a constant like 255
c = b*255
cv2.imwrite('skeleton.png', c)