import cv2
import numpy
from PIL import Image
from skimage.morphology  import label
from skimage.measure import regionprops
from skimage.feature import match_template

# Opening the image and converting it to grayscale.
image = Image.open('../Figures/airline_seating.png')
image = image.convert('L')
# Converting the input image into an ndarray.
image = numpy.asarray(image)
# Reading the template image.
temp = Image.open('../Figures/template1.png')
temp = temp.convert('L')
# Converting the template into an ndarray.
temp = numpy.asarray(temp)
# Performing template matching.
result = match_template(image, temp)
thresh = 0.7
# Thresholding the result from template
# matching considering pixel values where the
# normalized cross-correlation is greater than 0.7.
res = result > thresh
# Labeling the thresholded image.
c = label(res, background=0)
# Performing regionprops to count the
# number of label.
reprop = regionprops(c)
print("The number of seats are:", len(reprop))
# Converting the binary image to an 8-bit for storing.
res = res*255
# Converting the ndarray to image.
cv2.imwrite("../Figures/templatematching_output.png", res)
