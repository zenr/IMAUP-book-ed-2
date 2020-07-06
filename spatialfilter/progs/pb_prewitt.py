import cv2
from scipy import ndimage

# Opening the image.
a = cv2.imread('../Figures/cir.png')
# Converting a to grayscale .
a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
# Performing Prewitt filter.
b = ndimage.prewitt(a)
min_b, max_b = b.min(), b.max()
b = 255.0*(b-min_b)/(max_b-min_b)
# Saving b.
cv2.imwrite('../Figures/prewitt_cir.png', b)
