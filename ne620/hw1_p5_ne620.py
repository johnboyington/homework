#Homework 1 Problem 5
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.integrate as integrate

#input parameters
P = 3000.0E6 #Wth
MF_ratio = 1. / 9.
q_p = 400. #W/cm
q_pp = 125. #W/cm2
T_i = 290. #deg C
T_o = 330. #deg C
cp = 6400. #J/kgK
rho = 703.607E-6 #kg/cm3

#(a) calculate fuel radius
r = (q_p / (q_pp * 2 * np.pi))
print 'fuel radius', r

#(b) calculate lattice pitch
pitch = np.sqrt((MF_ratio + 1) * np.pi * r**2)
print 'pitch', pitch

#(c) calculate core volume and dimensions
L = ((4. * P * (pitch**2)) / q_p)**(1./3) #length of one rod
print 'L', L

A = np.pi * (L / 2.)**2
print 'area', A
V = A * L
print 'Volume', V

#(d) calculate core-averaged power density
P_density = P / V
print 'Power Density', P_density

#(e) calculate number of fuel elements
n = A / (pitch**2)
print 'n', n

#(f) calculate coolant mass flow rate
mdot = P / (cp * (T_o - T_i))
print 'mass flow', mdot

#(g) calculate mean coolant velocity
A_fuel = np.pi * (r**2) #cm2
A_water = A - (n * A_fuel) #cm2
Vdot = mdot / rho #cm3/s
vel = Vdot / A_water #cm/s
print 'Fuel Pin Area', A_fuel
print 'Moderator Area', A_water
print 'Volumetric flow', Vdot
print 'Velocity', vel


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