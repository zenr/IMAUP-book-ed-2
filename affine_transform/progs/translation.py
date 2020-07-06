import numpy as np
import scipy.misc, math
from scipy.misc.pilutil import Image
from skimage.transform import AffineTransform, warp

img = Image.open('../Figures/angiogram1.png').convert('L')
img1 = scipy.misc.fromimage(img)

# translate by 10 pixels in x and 4 pixels in y
transformation = AffineTransform(translation=(10, 4))
img2 = warp(img1, transformation)
im4 = scipy.misc.toimage(img2)
im4.save('../Figures/translate_output.png')
im4.show()
