import numpy as np
import scipy.ndimage
from PIL import Image
import cv2

# opening the image and converting it to grayscale
a = Image.open('../Figures/withcontrast1.png')
a = a.convert('L')
# Median filter is performed on the
# image to remove noise.
img = scipy.ndimage.filters.median_filter(a,size=5)
# Circles are determined using
# Hough circles transform.
circles = cv2.HoughCircles(img,
          cv2.HOUGH_GRADIENT,1,10,param1=100,
          param2=30,minRadius=10,maxRadius=30)
# circles image is rounded to unsigned integer 16.
circles = np.uint16(np.around(circles))
# For each detected circle.
for i in circles[0,:]:
	# An outer circle is drawn for visualization.
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
	# its center is marked
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
# Saving the image as houghcircles_output.png
cv2.imwrite('../Figures/houghcircles_output.png', img)
