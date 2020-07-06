import cv2
import scipy.ndimage

# Opening the image.
a = cv2.imread('../Figures/imagefor_laplacian.png')
# Performing Laplacian filter.
b = scipy.ndimage.filters.laplace(a,mode='reflect')
cv2.imwrite('../Figures/laplacian_new.png',b)   