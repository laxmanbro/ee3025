"""
@author: Bandi Sai Laxman 
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import soundfile as sf

# ..........................
#If using termux

import subprocess
import shlex

#...................................

x,F_s = sf.read('Sound_Noise.wav')
N = len(x)
y = np.zeros(N)
order = 4
cutoff_freq = 4000.0
sampling_freq = F_s

Wn = 2*cutoff_freq/sampling_freq
b,a = signal.butter(order, Wn, 'low')

'''
Rearranging the linear constant_coefficient difference equation we get the folowing Equation shown Below
'''
y[0] = (b[0]/a[0])*x[0]
y[1] = (1/a[0])*(b[0]*x[1]+b[1]*x[0] - a[1]*y[0])
y[2] = (1/a[0])*(b[0]*x[2]+b[1]*x[1]+b[2]*x[0]- 
		a[1]*y[1]-a[2]*y[0])

y[3] = (1/a[0])*(b[0]*x[3]+b[1]*x[2]+b[2]*x[1]+
		b[3]*x[0] - a[1]*y[2]-a[2]*y[1]-a[3]*y[0])
y[4] = (1/a[0])*(b[0]*x[4]+b[1]*x[3]+b[2]*x[2]+
		b[3]*x[1]+b[4]*x[0] - a[1]*y[3]-a[2]*y[2]-
		a[3]*y[1]-a[4]*y[0])

for i in range(5,N):
	y[i] = (1/a[0])*(b[0]*x[i]+b[1]*x[i-1]+b[2]*x[i-2]+
		b[3]*x[i-3]+b[4]*x[i-4] - a[1]*y[i-1]-a[2]*y[i-2]-
		a[3]*y[i-3]-a[4]*y[i-4])

sf.write('difference_filter.wav',y,F_s)

print("x", np.max(x), np.min(x))
print("y", np.max(y), np.min(y))

#subplots
plt.subplot(2, 1, 1)
plt.plot(x)
plt.title('Difference Eqs Filter Input-Output')
plt.ylabel('$x(N)$')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(y)
plt.xlabel('$N$')
plt.ylabel('$y(N)$')
plt.grid()


plt.savefig('../figs/plot_xy.pdf')
plt.savefig('../figs/plot_xy.eps')


#If using termux


# subprocess.run(shlex.split("termux-open ../figs/plot_xy.pdf"))

# else

plt.show()


