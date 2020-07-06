import cv2
import numpy as np

import numpy as np
from PIL import Image
from skimage.filters import frangi

img = cv2.imread('../Figures/angiogram1.png')
img1 = np.asarray(img)
img2 = frangi(img1, black_ridges=True)
img3 = 255*(img2-np.min(img2))/(np.max(img2)-np.min(img2))
cv2.imwrite('../Figures/frangi_output.png', img3)
