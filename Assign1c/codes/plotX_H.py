

"""
@author: Bandi Sai Laxman 
"""
import numpy as np
import soundfile as sf
from scipy import signal
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex

def convert_complx(var):
	var = str(var)[2:]
	var = var[0 : len(var) - 1]
	return complex(var.replace('+-', '-').replace('i', 'j'))

X = np.loadtxt('fft_x.dat', converters={0: convert_complx}, dtype = np.complex128, delimiter = '\n')
H = np.loadtxt('fft_h.dat', converters={0: convert_complx}, dtype = np.complex128, delimiter = '\n')
X = np.fft.fftshift(X)
H = np.fft.fftshift(H)
n = len(X)


plt.subplot(2,1,1)
plt.plot(np.linspace(-np.pi,np.pi,n),abs(X))
plt.grid()
plt.xlabel("$\omega$")
plt.ylabel("|X|")
plt.title("FFT - x[n]")

plt.subplot(2,1,2)
plt.plot(np.linspace(-np.pi,np.pi,len(H)),abs(H))
plt.grid()
plt.xlabel("$\omega$")
plt.ylabel("|H|")
plt.title("FFT - h[n]")
plt.tight_layout()

plt.savefig('../figs/fft_h.eps')
plt.savefig('../figs/fft_h.pdf')

#if using termux


#subprocess.run(shlex.splilt("termux-open ../Figures/Hk.pdf"))

#else
plt.show()

