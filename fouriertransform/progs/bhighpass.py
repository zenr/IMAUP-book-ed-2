import cv2
import numpy, math
import scipy.misc
import scipy.fftpack as fftim
from PIL import Image

# Opening the image.
a = cv2.imread('../Figures/endothelium.png')
# Converting the image to grayscale.
b = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
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
t1 = 1 # the order of BHPF
t2 = 2*t1    

# Defining the convolution function for BHPF.
for i in range(1,M):
    for j in range(1,N):
        r1 = (i-center1)**2+(j-center2)**2
        # Euclidean distance from 
        # origin is computed.
        r = math.sqrt(r1)
        # Using cut-off radius to 
        # eliminate low frequency.
        if 0 < r < d_0:   
            H[i,j] = 1/(1 + (r/d_0)**t2) 

# Converting H to an image.
H = Image.fromarray(H) 	
# performing the convolution 
con = d * H 
# computing the magnitude of the inverse FFT
e = abs(fftim.ifft2(con))
cv2.imwrite('../Figures/bhighpass_output.png', e)

