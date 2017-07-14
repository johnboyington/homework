#NE737 Homework 3

import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

###############################################################################
# PROBLEM 1
###############################################################################

#given data
t = np.array(range(11)) * 10
R = np.array([0, 46.1, 88.5, 101.2, 87.4, 71.8, 51.1, 34.9, 23.2, 14.2, 9.1])
tau = 14.5 #sec

tt = np.linspace(0, 100, 1000)
N = 3
S = 5500

#good values tau=14.5, N=3, S=5500



A = tt**(N-1)
B = sp.gamma(N) * (tau**N)
C = np.exp(-tt/tau)

crate = S * (A / B) * C



plt.figure()
plt.title("Response of a Radiotracer")
plt.xlabel("Time (sec)")
plt.ylabel("Response (cps)")
plt.axis([0, 110, 0, 120])

plt.plot(t, R, marker='o', label='data')
plt.plot(tt, crate, label='N tanks in series')

plt.legend()
plt.savefig('hw3p1ne737b.png')


