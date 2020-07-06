import numpy as np
from PIL import Image
import scipy.ndimage 

# Opening the image and converting it into grayscale.
a = Image.open('../figures/adaptive_example1.png').convert('L')
# Creating a structuring element.
footprint = np.ones((40,40))
# Performing grey opening.
b = scipy.ndimage.morphology.grey_opening(a, footprint=footprint)
# Converting ndarray to image.
c = Image.fromarray(b)
# Saving the image.
c.save('../figures/grey_opening_output_40.png')  