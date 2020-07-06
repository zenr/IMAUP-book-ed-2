import scipy.misc
import scipy.ndimage
from scipy.misc.pilutil import Image

# opening the image and converting it to grayscale
a = Image.open('../Figures/wave.png').convert('L')
# performing maximum filter
b = scipy.ndimage.filters.maximum_filter(a, size=5)
# b is converted from an ndarray to an image
b = scipy.misc.toimage(b)
b.save('../Figures/maxo.png')
