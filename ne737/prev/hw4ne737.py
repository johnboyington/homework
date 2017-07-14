#ne737 hw4

import numpy as np
import matplotlib.pyplot as plt

###############################################################################
#                             PROBLEM 1
###############################################################################

i = np.array(range(38)) + 815

ci = np.array([189, 171, 182, 170, 191, 184, 176, 188, 209, 208, 251, 268, 343, 387, 473, 540, 581, 652, 655, 667, 619, 588, 487, 415, 370, 285, 267, 199, 196, 183, 158, 150, 162, 139, 160, 153, 138, 145])

m = -0.8
b = 830
B = m*i + b

plt.figure(0)
plt.title("Response of an irradiated piece of Gold Jewelery")
plt.xlabel("Channel, i")
plt.ylabel("$C_i$ (counts/channel)")
plt.xlim(815, 853)
plt.ylim(0, 700)
plt.plot(i, ci)
plt.plot(i, B)
plt.savefig('p1.png')

pk = ci - B
Cjk = np.sum(pk)
Na = 6.022E23
m = 0.003 #g
eta = 0.005
flux_t = 10 ** 12 #cm-2s-2
to = 3600 #s
tw = 3600 #s
tc = 3600 #s
xs = 87.46*1E-24

#still need
Ai =  197 #atomic mass of precursor isotope i in element x (g mol-1)
lam = 2.9776E-6 #decay constant of radioisotope of interest (s-1)
pi = 1 #abundance of precursor isotope i in the element of interest
fk = 1 #branching ratio of the gamma ray k in the radioisotope of interest

A = Cjk * Ai * lam

Ta = (1 - np.exp(-lam * to))**(-1)
Tb = np.exp(lam * tw)
Tc = (1 - np.exp(-lam * tc))**(-1)
B = Ta * Tb * Tc
C = Na * m * pi * fk * eta * flux_t * xs

mux = (A / C) * B

print mux, mux * m

error = (((mux / Cjk)**2)*Cjk)**(0.5)

print error, error * m