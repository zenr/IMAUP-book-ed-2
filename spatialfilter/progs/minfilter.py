import cv2
import scipy.ndimage

# opening the image and converting it to grayscale
a = cv2.imread('../Figures/wave.png')

# performing minimum filter
b = scipy.ndimage.filters.minimum_filter(a, size=5)
# saving b as mino.png
cv2.imwrite('../Figures/mino.png', b)
