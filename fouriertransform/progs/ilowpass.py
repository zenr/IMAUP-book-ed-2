import cv2
import numpy, math
import scipy.fftpack as fftim   
from PIL import Image

# Opening the image and converting it to grayscale.
b = Image.open('../Figures/fft1.png').convert('L') 
# Performing FFT.
c = fftim.fft2(b)  
# Shifting the Fourier frequency image.
d = fftim.fftshift(c) 

# Intializing variables for convolution function.
M = d.shape[0]
N = d.shape[1]  
# H is defined and 
# values in H are initialized to 1.
H = numpy.ones((M,N)) 
center1 = M/2
center2 = N/2
d_0 = 30.0 # cut-off radius

# Defining the convolution function for ILPF.
for i in range(1,M):
    for j in range(1,N):
        r1 = (i-center1)**2+(j-center2)**2
        # Euclidean distance from 
        # origin is computed.
        r = math.sqrt(r1) 
        # Using cut-off radius to eliminate 
        # high frequency.
        if r > d_0:
            H[i,j] = 0.0
# Converting H to an image.
H =  Image.fromarray(H) 
# Performing the convolution.
con = d * H 
# Computing the magnitude of the inverse FFT.
e = abs(fftim.ifft2(con)) 
# Saving e as ilowpass_output.png in
# Figures folder .
cv2.imwrite('../Figures/ilowpass_output.png', e)
