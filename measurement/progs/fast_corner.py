import numpy as np
from PIL import Image
from skimage.feature import corner_peaks
from skimage.feature import corner_subpix, corner_fast
from matplotlib import pyplot as plt

# Image is opened and is converted to grayscale.
img = Image.open('../Figures/corner_detector.png').convert('L')
# img is converted to an ndarray.
img1 = np.asarray(img)

corner_response = corner_fast(img1)
cpv = corner_peaks(corner_response, min_distance=50)
corners_subpix_val = corner_subpix(img1, cpv, window_size=13)
fig, ax = plt.subplots()
ax.imshow(img1, interpolation='nearest', cmap=plt.cm.gray)
x = corners_subpix_val[:, 1]
y = corners_subpix_val[:, 0]
ax.plot(x, y, 'ob', markersize=10)
ax.axis('off')
plt.savefig('../Figures/corner_fast_detector_output.png', dpi=300)
plt.show()
