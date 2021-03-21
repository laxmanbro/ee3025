
"""
@author: Bandi Sai Laxman 
"""

import numpy as np
import soundfile as sf
from scipy import signal
import matplotlib.pyplot as plt


#...............................
#If using termux
import subprocess
import shlex
#......................

x,F_s = sf.read('Sound_Noise.wav')
n = len(x)
y = np.zeros(n)
order = 4
cutoff_freq = 4000.0
samp_freq = F_s

Wn = 2*cutoff_freq/samp_freq
b,a = signal.butter(order,Wn,'low')


h_n = np.zeros(n)
h_n[0] = (b[0]/a[0])
h_n[1] = (1/a[0])*(b[1]-a[1]*h_n[0])   
#y(n-k) = h(n-k) for all k=0,1,2,3,4, so we use y(n)-same expression
h_n[2] = (1/a[0])*(b[2]-a[1]*h_n[1]-a[2]*h_n[0])
h_n[3] = (1/a[0])*(b[3]-a[1]*h_n[2]-a[2]*h_n[1]-a[3]*h_n[0])
h_n[4] = (1/a[0])*(b[4]-a[1]*h_n[3]-a[2]*h_n[2]-a[3]*h_n[1]
		-a[4]*h_n[0])

for i in range(5,n):
	h_n[i] = (1/a[0])*(-a[1]*h_n[i-1]-a[2]*h_n[i-2]-a[3]*h_n[i-3]-
			a[4]*h_n[i-4])


plt.plot(h_n[0:99])
plt.title( ' Impulse Response')
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.grid() 

plt.savefig('../figs/impulse_response.pdf')
plt.savefig('../figs/impulse_response.eps')

#If using termux


# subprocess.run(shlex.split("termux-open ../figs/impulse_response.pdf"))

#else

plt.show()

