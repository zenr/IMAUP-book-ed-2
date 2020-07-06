import numpy as np
import scipy.misc, math
from scipy.misc.pilutil import Image
from skimage.transform import AffineTransform, warp

img = Image.open('../Figures/angiogram1.png').convert('L')
img1 = scipy.misc.fromimage(img)

transformation = AffineTransform(scale=(0.3, 0.3))

# nearest neighbor order = 0
img2 = warp(img1, transformation, order=0)
im4 = scipy.misc.toimage(img2)
im4.save('../Figures/interpolate_nn_output.png')
im4.show()

# bi-linear order = 1
img2 = warp(img1, transformation, order=1) # default
im4 = scipy.misc.toimage(img2)
im4.save('../Figures/interpolate_bilinear_output.png')
im4.show()

#bi-quadratic order = 2
img2 = warp(img1, transformation, order=2)
im4 = scipy.misc.toimage(img2)
im4.save('../Figures/interpolate_biquadratic_output.png')
im4.show()

#bi-cubic order = 3
img2 = warp(img1, transformation, order=3)
im4 = scipy.misc.toimage(img2)
im4.save('../Figures/interpolate_bicubic_output.png')
im4.show()
