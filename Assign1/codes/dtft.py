
"""
@author: Bandi Sai Laxman
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import soundfile as sf



#...........................
#If using termux
import subprocess
import shlex
#.......................

#DTdtft
def impulse(z,num,den):
    numr = np.polyval(num,pow(z,-1))
    denr = np.polyval(den,pow(z,-1))
    return numr/denr

x,fs = sf.read('Sound_Noise.wav')
samp_freq = fs
order = 4
cutoff_freq = 4000.0
Wn = 2*cutoff_freq/samp_freq

b, a = signal.butter(order,Wn,'low')

#input and output
omega = np.linspace(-np.pi,np.pi,len(x),endpoint=True)

#subplots
plt.plot(omega,abs(impulse(np.exp(1j*omega),b,a)))
plt.title('Frequency Impulse Response')
plt.xlabel('$w$')
plt.ylabel('$impulse(jw)$')
plt.grid()# minor

#If using termux

plt.savefig('../figs/dtft.pdf')
plt.savefig('../figs/dtft.eps')
subprocess.run(shlex.split("termux-open ../figs/dtft.pdf"))

#else
# plt.show()
