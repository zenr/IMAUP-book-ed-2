import numpy as np
from PIL import Image
import scipy.ndimage

# Opening the image and converting it into grayscale.
a = Image.open('../figures/sem3.png').convert('L')
# Creating a structuring element.
footprint = np.ones((15,15))
# Performing grey dilation.
b = scipy.ndimage.morphology.grey_dilation(a, footprint=footprint)
# Converting ndarray to image.
c = Image.fromarray(b)
# Saving the image.
c.save('../figures/grey_dilation_output_15.png')
