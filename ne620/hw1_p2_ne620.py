#Homework 1 Problem 2
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.integrate as integrate



#steps to solve
#1 Q = m'*c*dT to find m'
#2 pump power pressure drop * volumetric flowrate


#input parameters
Qdot = 3817.E3 #kWth  Core Power
dTcore = 31. #deg Celsius  Temperature change in the core
delPsi = 113. #psi  reactor coolant pressure drop
cp_w = 5.329 #kJ/(kg*K) specific heat of water at 283degC 10MPa
rho = 1000. #kg/m3 density of water

#convert psi to kN/m2
delP = 6.89476 * delPsi #kN/m2

#calculate mdot
mdot = Qdot / (cp_w * dTcore) #kg/s mass flow rate of the water
print mdot

#calculate Vdot
Vdot = mdot / rho #m3/s  volumetric flow rate

#calculate P
P = delP * Vdot #kW = kN/m2 * m3/s
print P



#plt.figure()
#plt.plot(z, q_p(z))
#plt.title("Axial Linear Power Shape")
#plt.xlabel("Axial Distance (m)")
#plt.ylabel("Fission Rate (s$^{-1}$)")
#plt.xlim(-1, 5)
#plt.ylim(0, 45)
##plt.xscale('log')
##plt.yscale('log')
#plt.show()