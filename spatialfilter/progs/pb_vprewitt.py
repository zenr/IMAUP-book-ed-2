import cv2
from skimage import filters
import matplotlib.pyplot as plt

# Opening the image.
a = cv2.imread('../Figures/cir.png')
# Converting a to grayscale .
a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
# Performing vertical Prewitt.
b = filters.prewitt_v(a)
min_b, max_b = b.min(), b.max()
b = 255*(b-min_b)/(max_b-min_b)
# Saving b .
cv2.imwrite('../Figures/prewitt_vcir.png', b)
# Displaying b.
plt.imshow(b, 'gray')
plt.show()
