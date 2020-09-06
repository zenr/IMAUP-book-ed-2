import scipy.ndimage 
import cv2

# opening the image and converting it to a greyscale image
a = cv2.imread('figure/ct_saltandpepper.png')
a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)

# performing minimum filter
b = scipy.ndimage.filters.minimum_filter(a,size=5, 
	footprint=None,output=None,mode='reflect',  
	cval=0.0,origin=0)

cv2.imwrite('min_ctsaltandpepper.png', b)
  