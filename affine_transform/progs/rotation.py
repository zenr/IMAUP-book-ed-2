import numpy as np
import scipy.misc, math
from scipy.misc.pilutil import Image
from skimage.transform import AffineTransform, warp

img = Image.open('../Figures/angiogram1.png').convert('L')
img1 = scipy.misc.fromimage(img)

# rotation angle in radians
transformation = AffineTransform(rotation=0.1)
img2 = warp(img1, transformation)
im4 = scipy.misc.toimage(img2)
im4.save('../Figures/rotate_output.png')
im4.show()
