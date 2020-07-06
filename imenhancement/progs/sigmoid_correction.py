import cv2
from skimage.exposure import adjust_sigmoid

# Reading the image.
img1 = cv2.imread('../Figures/hequalization_input.png')
# Applying Sigmoid correction.
img2 =  adjust_sigmoid(img1, gain=15)
# Saving img2.
cv2.imwrite('../Figures/sigmoid_output.png', img2)
