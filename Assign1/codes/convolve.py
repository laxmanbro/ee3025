
"""
@author: Bandi Sai Laxman 
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import soundfile as sf


# ........................................
# If using termux

import subprocess
import shlex

#..........................

def circular_convolv(signal, kernel): 
  return np.real(np.fft.ifft( np.fft.fft(signal)*np.fft.fft(kernel)))

x,F_s = sf.read('Sound_Noise.wav')
n = len(x)
y = np.zeros(n)
order = 4
cutoff_freq = 4000.0
samp_freq = F_s

Wn = 2*cutoff_freq/samp_freq
b,a = signal.butter(order,Wn,'low')

h = np.zeros(n)
h[0] = (b[0]/a[0])
h[1] = (1/a[0])*(b[1]-a[1]*h[0])
h[2] = (1/a[0])*(b[2]-a[1]*h[1]-a[2]*h[0])
h[3] = (1/a[0])*(b[3]-a[1]*h[2]-a[2]*h[1]-a[3]*h[0])
h[4] = (1/a[0])*(b[4]-a[1]*h[3]-a[2]*h[2]-a[3]*h[1]
		-a[4]*h[0])
for i in range(5,n):
	h[i] = (1/a[0])*(-a[1]*h[i-1]-a[2]*h[i-2]-a[3]*h[i-3]-
			a[4]*h[i-4])

y = np.zeros(n)
y = circular_convolv(x,h)   #np.convolve results in linear convolution
sf.write('convolve_music.wav', y, F_s)
#subplots
plt.plot(y)
plt.title('Filter output using convolution')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor

#If using termux

plt.savefig('../figs/convolve.pdf')
plt.savefig('../figs/convolve.eps')
subprocess.run(shlex.split("termux-open ../figs/convolve.pdf"))

#else
#plt.show()

