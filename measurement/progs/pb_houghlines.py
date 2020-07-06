import cv2
import numpy as np

# Opening the image.
im = cv2.imread('../Figures/hlines.png')
# Converting the image to grayscale.
a1 = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# Thresholding the image to obtain 
# only foreground pixels.
thresh, b1 = cv2.threshold(a1, 0, 255,
            cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

cv2.imwrite('../Figures/hlines_thresh.png', b1)
# Performing the Hough lines transform.
lines = cv2.HoughLines(b1, 10, np.pi/20, 200)
for rho, theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(im,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imwrite('../Figures/houghlines_output.png', im)
    
# Printing the lines: distance and angle in radians.
print(lines)
