import scipy.fftpack as fftim
from PIL import Image

# Opening the image and converting it to grayscale.
b = Image.open('../Figures/fft1.png').convert('L') 
# Performing FFT.
c = abs(fftim.fft2(b))
# Shifting the Fourier frequency image.
d = fftim.fftshift(c)
# Converting the d to floating type and saving it 
# as fft1_output.raw in Figures folder.
d.astype('float').tofile('../Figures/fft1_output.raw')
