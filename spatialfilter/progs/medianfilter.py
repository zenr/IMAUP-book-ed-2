import cv2
import scipy.ndimage

# Opening the image and converting it to grayscale.
a = cv2.imread('../Figures/ct_saltandpepper.png')
# Converting the image to grayscale.
a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
# Performing the median filter.
b = scipy.ndimage.filters.median_filter(a, size=5)
# Saving b as median_output.png in Figures folder
cv2.imwrite('../Figures/median_output.png', b)
