import cv2
 
# Opening the image.
a = cv2.imread('../Figures/maps1.png')
# Performing Canny edge filter.
b = cv2.Canny(a, 100, 200)
# Saving b.
cv2.imwrite('../Figures/canny_output.png', b) 