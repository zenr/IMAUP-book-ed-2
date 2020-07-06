import cv2

# Opening the image.
im = cv2.imread('../Figures/hequalization_input.png')
# Finding the maximum and minimum pixel values
b = im.max()
a = im.min()
print(a,b)
# Converting im1 to float.
c = im.astype(float)
# Contrast stretching transformation.
im1 = 255.0*(c-a)/(b-a+0.0000001)
# Saving im2 as contrast_output.png in
# Figures folder 
cv2.imwrite('../Figures/contrast_output2.png', im1) 