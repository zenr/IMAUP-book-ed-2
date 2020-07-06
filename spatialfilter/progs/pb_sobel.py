import cv2
from scipy import ndimage

# Opening the image.
a = cv2.imread('../Figures/cir.png')
# Converting a to grayscale .
a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
# Performing Sobel filter.
b = ndimage.sobel(a)
# Saving b.
cv2.imwrite('../Figures/sobel_cir.png', b)
