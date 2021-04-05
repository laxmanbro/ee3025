"""
@author: Bandi Sai Laxman 
"""
import soundfile as sf
import numpy as np
from scipy import signal



#If using termux
import subprocess
import shlex

x, fs = sf.read('Sound_Noise.wav')

N = int(2 ** np.floor(np.log2(len(x))))
f = open("x.dat", "w") 
for i in range(N):
    f.write(str(x[i]) + "\n")
f.close()
