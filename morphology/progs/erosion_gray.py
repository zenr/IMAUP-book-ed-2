import numpy as np
from PIL import Image
import scipy.ndimage 

# Opening the image and converting it into grayscale.
a = Image.open('../figures/sem3.png').convert('L')
# Creating a structuring element.
footprint = np.ones((15, 15))
# Performing grey erosion.
b = scipy.ndimage.morphology.grey_erosion(a, footprint=footprint)
# Converting ndarray to image.
c = Image.fromarray(b)
# Saving the image.
c.save('../figures/grey_erosion_output_15.png')  