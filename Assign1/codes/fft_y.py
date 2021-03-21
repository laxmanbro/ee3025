
"""
@author: Bandi Sai Laxman 
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import soundfile as sf


#.....................................
#If using termux
import subprocess
import shlex
#..............................

def impulse(z,num,den):
    numr = np.polyval(num,pow(z,-1))
    denr = np.polyval(den,pow(z,-1))
    return numr/denr

x,F_s = sf.read('Sound_Noise.wav')
samp_freq = F_s
order = 4
cutoff_freq = 4000.0
Wn = 2*cutoff_freq/samp_freq

b,a = signal.butter(order,Wn,'low')

n = len(x)
y = np.zeros(n)

omg = np.linspace(-np.pi,np.pi,n,endpoint=True)
z = np.exp(1j * omg)
impulse = impulse(z,b,a)
X = np.fft.fftshift(np.fft.fft(x))
Y = np.multiply(X,impulse)
y = np.fft.ifft(np.fft.ifftshift(Y))
sf.write('fft_music.wav',np.real(y),F_s)

plt.plot(np.real(y))
plt.title('Filter output IFFT')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor

#If using termux

plt.savefig('../figs/fft_y.pdf')
plt.savefig('../figs/fft_y.eps')
subprocess.run(shlex.split("termux-open ../figs/fft_y.pdf"))

#else

# plt.show()
