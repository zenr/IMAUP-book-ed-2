import numpy as np
from PIL import Image
import scipy.ndimage 

# Opening the image and converting it into grayscale.
a = Image.open('../figures/adaptive_example1.png').convert('L')
a = np.asarray(a)
# Creating a structuring element.
fp = np.ones((40,40))
# Performing grey closing.
bg = scipy.ndimage.morphology.grey_closing(a, footprint=fp)
# bg represents the background. 
# We will subtract bg from a to remove the background in a.
bg_free = (a.astype(np.float64) - bg.astype(np.float64))
# We rescale bg_free to 0 to 255.
denom = (bg_free.max()-bg_free.min())
bg_free_norm = (bg_free - bg_free.min())*255/denom
# Converting bg_free_norm to uint8.
bg_free_norm = bg_free_norm.astype(np.uint8)
# Converting bg_free_norm and bg to images.
bg_free_norm = Image.fromarray(bg_free_norm)
bg = Image.fromarray(bg)
# Saving the background image.
bg.save('../figures/grey_closing_out_40.png')  
# Saving the bg_free_norm image.
bg_free_norm.save('../figures/closing_bgfree.png')  