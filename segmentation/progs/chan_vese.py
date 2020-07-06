from PIL import Image
import matplotlib.pyplot as plt
from skimage.segmentation import chan_vese
import numpy as np

# Opening the image and converting it into grayscale
img = Image.open('../Figures/imageinverse_input.png').convert('L')
img = np.array(img)

cv1 = chan_vese(img, mu=0.1)
cv2 = chan_vese(img, mu=0.3)
cv3 = chan_vese(img, mu=0.6)

fig, axes = plt.subplots(2, 2, figsize=(8, 8))
ax = axes.flatten()
ax[0].imshow(img, cmap="gray")
ax[0].set_axis_off()
ax[0].set_title("Original Image", fontsize=12)

ax[1].imshow(cv1, cmap="gray")
ax[1].set_axis_off()
ax[1].set_title("mu=0.1", fontsize=12)

ax[2].imshow(cv2, cmap="gray")
ax[2].set_axis_off()
ax[2].set_title("mu=0.3", fontsize=12)


ax[3].imshow(cv3, cmap="gray")
ax[3].set_axis_off()
ax[3].set_title("mu=0.6", fontsize=12)
plt.show()
