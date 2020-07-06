import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from skimage.feature import corner_harris
from skimage.feature import corner_peaks, corner_subpix

# Opening image and converting it into grayscale.
img = Image.open('../Figures/corner_detector.png').convert('L')
# img is converted to an ndarray.
img1 = np.asarray(img)

# Detecting corners using Harris.
corner_response = corner_harris(img1, k=0.2)
# Detecting peak values.
corners_peak_val = corner_peaks(corner_response, 50)

corners_subpix_val = corner_subpix(img1, corners_peak_val, 13)
# Defining a subplot.
fig, ax = plt.subplots()
# Displaying the image.
ax.imshow(img1, interpolation='nearest', cmap=plt.cm.gray)
x = corners_subpix_val[:, 1]
y = corners_subpix_val[:, 0]
ax.plot(x, y, 'ob', markersize=10)
ax.axis('off')
# Saving the image.
plt.savefig('../Figures/corner_harris_detector_output.png', dpi=300)
plt.show()
