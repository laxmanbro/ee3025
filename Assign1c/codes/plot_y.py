"""
@author: Bandi Sai Laxman 
"""

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

#If using termux
import subprocess
import shlex

y= np.loadtxt('ifft_y.dat')
input_file, fs = sf.read('Sound_Noise.wav')
# wirting the final sound file 
sf.write('SoundFiltered_C.wav', y, fs)

plt.plot(y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor
plt.title("IFFT of Y(K)")

plt.tight_layout()

#if using termux
plt.savefig('../figs/ifft_y.eps')
plt.savefig('../figs/ifft_y.pdf')

#subprocess.run(shlex.splilt("termux-open ../Figures/ifft_yn.pdf"))

#else
plt.show()
