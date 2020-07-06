import cv2
import numpy as np
import scipy.ndimage

# Opening the image using cv2.
a = cv2.imread('../Figures/ultrasound_muscle.png')
# Converting the image to grayscale.
a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)

# Initializing the filter of size 5 by 5.
# The filter is divided by 25 for normalization.
k = np.ones((5,5))/25
# performing convolution
b = scipy.ndimage.filters.convolve(a, k)
# Writing b to a file.
cv2.imwrite('../Figures/mean_output.png', b)
