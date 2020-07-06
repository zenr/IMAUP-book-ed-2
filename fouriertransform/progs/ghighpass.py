import cv2
import numpy, math
import scipy.fftpack as fftim
from PIL import Image

# Opening the image and converting it to grayscale.
a = Image.open('../Figures/endothelium.png').convert('L') 
# Performing FFT.
b = fftim.fft2(a) 
# Shifting the Fourier frequency image. 
c = fftim.fftshift(b) 

# Intializing variables for convolution function.
M = c.shape[0] 
N = c.shape[1]
# H is defined and values in H are initialized to 1.
H = numpy.ones((M,N)) 
center1 = M/2   
center2 = N/2
d_0 = 30.0 # cut-off radius
t1 = 2*d_0

# Defining the convolution function for GHPF.
for i in range(1,M):
    for j in range(1,N):
        r1 = (i-center1)**2+(j-center2)**2
        # Euclidean distance from 
        # origin is computed.
        r = math.sqrt(r1) 
        # Using cut-off radius to 
        # eliminate low frequency.
        if 0 < r < d_0:
            H[i,j] = 1 - math.exp(-r**2/t1**2)

# Converting H to an image.
H = Image.fromarray(H) 
# Performing the convolution.
con = c * H 
# Computing the magnitude of the inverse FFT.
e = abs(fftim.ifft2(con)) 
# Saving the image as ghighpass_output.png in
# Figures folder.
cv2.imwrite('../Figures/ghighpass_output.png', e)
