import cv2
import numpy, math

# Opening the image.
a = cv2.imread('../Figures/bse.png')
# a is converted to type float.
b1 = a.astype(float)
# Maximum value in b1 is determined.
b2 = numpy.max(b1)
# Performing the log transformation.
c = (255.0*numpy.log(1+b1))/numpy.log(1+b2)
# c is converted to type int.
c1 = c.astype(int)
# Saving c1 as logtransform_output.png.
cv2.imwrite('../Figures/logtransform_output.png', c1)