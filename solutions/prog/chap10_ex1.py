import math
from skimage.morphology  import label
from skimage.measure import regionprops
import cv2

# opening the image and converting it to grayscale 
a = cv2.imread('figure/houghcircles_segmented.png')
a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)

# labelling is preformed on a
c = label(a)

# c1 is saved as label_output.png
cv2.imwrite('label_output.png', c)

# on the labelled image c, regionprops is performed
d = regionprops(c)


print("The diameter of the circles are: ")
for props in d:
    print(2*math.sqrt(props['Area']/math.pi))
