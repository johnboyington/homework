#this code will help me with the ne620 takehome final

import numpy as np
import matplotlib.pyplot as plt

D_fuel = .037 #m fuel diameter
R_fuel = D_fuel / 2. #cm fuel radius
pitch = 0.04 #m equilateral triangule side
t_clad = .0005 #m cladding thickness

A_tri = (np.sqrt(3.) / 4) * (pitch**2) #cm2 triangle area
A_rod = np.pi*((D_fuel / 2.)**2) #cm2 area of a fuel rod
A_flow = 2 * (A_tri - ((0.5) * A_rod)) #cm2 flow area for two rods
C_fuel = np.pi * D_fuel #cm2 fuel circumference
p_wet = 4 * (pitch - D_fuel) +  C_fuel #cm wetted perimeter
p_fuel = np.pi * (D_fuel - (2 * t_clad)) #cm fuel perimeter

print A_tri


D_hyd = (4 * A_flow) / p_wet
D_heat = (4 * A_flow) / p_fuel

print 'The flow area is {} m^2.'.format(A_flow)
print 'The hydraulic diameter is {} m.'.format(D_hyd)
print 'The heated diameter is {} m.'.format(D_heat)

PF = 1.2          #radial power factor
n_bund = 85       #fuel bundles
P_tot = 1.25E6    #Wth

P_avg = P_tot / n_bund  # average power per rod [W]
P_peak = P_avg * PF     # hottest fuel channel

print 'The peak channel power is {} Wth.'.format(P_peak)

n = np.linspace(0, np.pi, 30)

prof = np.sin(n)

profile = prof / np.sum(prof)

print profile

for ii in range(len(profile)):
    print '177717{:2}           900      {:f}      0.0      0.0             {}'.format(ii+1, profile[ii], ii+1)