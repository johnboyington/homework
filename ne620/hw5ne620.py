import numpy as np
import matplotlib.pyplot as plt


###############################################################################
#                               PROBLEM 2
###############################################################################

def MDOT(A, g, L, K, p2ph, pc):
    BB = (g * L) / K
    CC = p2ph * (pc - p2ph)
    m = A * np.sqrt(BB * CC)
    return m

A = 0.1 #m2
K = 20
L = 5 #m
g = 9.81 #m/s2
pc = 821.9  #kg/m3
ph = 15 #kg/m3
x = np.linspace(0.001, 0.999, 1000)
p2ph = 1 /((1 - x) * (1 / pc) + (x / ph))

M = MDOT(A, g, L, K, p2ph, pc)



plt.figure()
plt.plot(x, M)
plt.title("Slip in the Homogeneous Model")
plt.xlabel("Q (relative)")
plt.ylabel("Mass Flow Rate")
plt.xlim(0, 1)
plt.ylim(0, 70)
plt.legend()
plt.show()
plt.savefig('ne620hw5p2.png')











###############################################################################
#                               PROBLEM 3
###############################################################################

#def Slip(a, pl, pv, x):
#    S = ((1/a) - 1) * (pl / pv) * (x / (1 - x))
#    return S
#
#def dfAlpha(Co, pl, pv, G, ugi, x):
#    AA = ((1-x) * pv) / (pl * x)
#    BB = (pv * ugi) / (G * x)    
#    A = 1 / ((Co * (1 + AA)) + BB)
#    return A
#
#G = 1200
#C = 1.13
#rhol = 739.72
#rhov = 36.52
#qual = np.linspace(0, 0.999, 1000)
#alpha = 0.586
#u = 0.245
#
#Sl = Slip(dfAlpha(C, rhol, rhov, G, u, qual), rhol, rhov, qual)
#
#plt.figure()
#plt.plot(qual, Sl)
#plt.title("Slip in the Homogeneous Model")
#plt.xlabel("Quality")
#plt.ylabel("Slip")
#plt.xlim(0, 1)
#plt.ylim(0, 100)
#plt.legend()
#plt.show()
#plt.savefig('ne620hw5p3.png')