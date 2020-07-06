import cv2
import scipy.ndimage

# Opening the image.
a = cv2.imread('../Figures/vhuman_t1.png')
# Performing Laplacian of Gaussian.
b = scipy.ndimage.filters.gaussian_laplace(a, sigma=1, mode='reflect')
cv2.imwrite('../Figures/log_vh1.png', b)   