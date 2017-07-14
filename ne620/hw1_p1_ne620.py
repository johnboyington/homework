#Homework 1 Problem 1
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.integrate as integrate

def alps(qq_pref, aa, LL):
    return lambda zz: qq_pref * np.exp(-((aa * zz) / LL)) * np.sin((np.pi*zz)/LL)



#input parameters
CBP = 9319. #kW
a = 1.96
L = 3.81 #m
z = np.arange(0, L, 0.001)
q_pref = 97.5693 #kw/m (found by guessing and checking)
n = 62. #number of fuel rods



#axial linear power shape
q_p = alps(q_pref, a, L)
print max(q_p(z))

qr = integrate.quad(q_p, 0, L)
print qr

qtot = n * qr[0]
print qtot

qpr = CBP / qtot
print qpr
#calculate minimum critical power ratio
#MCPR = CP / OP
#print MCPR


plt.figure()
plt.plot(z, q_p(z))
plt.title("Axial Linear Power Shape")
plt.xlabel("Axial Distance (m)")
plt.ylabel("Fission Rate (s$^{-1}$)")
plt.xlim(-1, 5)
plt.ylim(0, 45)
#plt.xscale('log')
#plt.yscale('log')
plt.show()