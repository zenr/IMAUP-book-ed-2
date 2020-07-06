from PIL import Image
import numpy as np
import scipy.ndimage as snd
import cv2

# Opening the image and converting it to grayscale.
a = Image.open('../figures/thickening_input.png').convert('L')
a = np.array(a)

# Defining the structuring element.
structure1 = np.array([[1, 1, 0], [1, 1, 1],
             [1, 1, 1]])
# Performing the binary hit-or-miss.
b = snd.morphology.binary_hit_or_miss(a, structure1=structure1)
# Saving the image as 8-bit as b is a
# binary image of dtype=bool
cv2.imwrite('../figures/hitormiss_output2.png', b*255)
