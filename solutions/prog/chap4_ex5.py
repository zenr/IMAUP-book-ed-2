import scipy.ndimage 
import cv2

# opening the image and converting it to a greyscale image
a = cv2.imread('figure/spinwheel.png')
a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)

# performing Laplacian of Gaussian with sigma = 0.9
im1 = scipy.ndimage.filters.gaussian_laplace(a,0.9,mode='reflect')
# performing Laplacian of Gaussian with sigma = 1.3
im2 = scipy.ndimage.filters.gaussian_laplace(a,1.3,mode='reflect')
# determining the difference for obtaining edge
b = im1-im2

cv2.imwrite('diff_log.png', b)   