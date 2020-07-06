import cv2
import numpy
from PIL import Image 
from skimage.filters.thresholding import threshold_otsu

# Opening the image and converting it to grayscale
a = Image.open('../Figures/sem3.png').convert('L')
a = numpy.asarray(a)
thresh = threshold_otsu(a)
# Pixels with intensity greater than the
# "threshold" are kept.
b = 255*(a > thresh)
# Saving the image.
cv2.imwrite('../Figures/otsu_output.png', b)