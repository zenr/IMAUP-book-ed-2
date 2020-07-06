import cv2


# Opening the image.
im = cv2.imread('../Figures/imageinverse_input.png')
# Performing the inversion operation
im2 = 255 - im
# Saving the image as imageinverse_output.png in
# Figures folder.
cv2.imwrite('../Figures/imageinverse_output.png', im2)
