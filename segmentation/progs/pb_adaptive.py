import cv2
import numpy
from PIL import Image
from skimage.filters import threshold_local

# Opening the image and converting it to grayscale.
a = Image.open('../Figures/adaptive_example1.png'). \
	convert('L')
a = numpy.asarray(a)
# Performing adaptive thresholding. 
b = cv2.adaptiveThreshold(a,a.max(),\
	cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,21,10)
# Saving the image as adaptive_output.png 
# in the folder Figures. 
cv2.imwrite('../Figures/adaptive_output.png', b)