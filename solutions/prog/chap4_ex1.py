import numpy as np 
import scipy.ndimage 
import cv2

# opening the image and converting it to a greyscale image
a = cv2.imread('figure/ct_saltandpepper.png')
a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)

# initializing the filter of size 5 by 5
# the filter is divided by 25 for normalization 
k = np.ones((5,5))/25
# performing convolution
b = scipy.ndimage.filters.convolve(a, k) 
 
cv2.imwrite('mean_ctsaltandpepper.png', b)
