#plots for p1 ne620 final

import numpy as np
import matplotlib.pyplot as plt\

httemp = np.loadtxt('httemp.txt')
tempf = np.loadtxt('tempf.txt')
velf = np.loadtxt('velf.txt')
z = np.array(range(30)) * (0.381 / 30)

vel = np.average(velf)

#dittus-boelter equation
D = 0.00968288069038 #m
nn = 0.4
mu = 8.9E-4 #Pa*s
rho = 1000 #kg/m3
Re_D = (rho * vel * D) / mu
print Re_D
Pr = 7.01 #water
k = 14.83 #W/(m*K)

Nu_D = 0.023 * (Re_D**(4./5.)) * (Pr ** nn)
print Nu_D
h = (Nu_D * k) / D
print h

A_flow = 0.000310430560364
L = 0.381 #m
Q = 1.7647E4 #W
n = np.linspace(0, np.pi, 30)
prof = np.sin(n)
profile = prof / np.sum(prof)
qpp = Q * profile
mdot = rho * vel * A_flow
Ti = 310.15 
Cp = 4180 #J/kgK
A_heat = np.pi * 0.010979
qop = (Q * np.pi) / (2 * L)

Tc = (((qop * L) / (mdot * Cp * np.pi)) * (1.0 - np.cos((np.pi * z) / L))) + Ti

print len(qpp), len(Tc), qop
Tw = ((qop * np.sin(np.pi * z / L)) / (h * A_heat)) + Tc

print vel



plt.figure(0)
plt.title('Comparison of Coolant & Cladding Temperatures')
plt.ylim(300, 450)
plt.xlabel('Axial Position [$m$]')
plt.ylabel('Temperature [$deg K$]')
plt.plot(z, httemp, label='Tclad RELAP')
plt.plot(z, tempf, label='Tcoolant RELAP')
plt.plot(z, Tc, label='Tcoolant Analytical')
plt.plot(z, Tw, label='Tclad Analytical')
plt.legend()
plt.savefig('temps.png')