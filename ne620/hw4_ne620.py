import numpy as np
import matplotlib.pyplot as plt

###############################################################################
#                             PROBLEM 1
###############################################################################


L = 10.0   #m
D = 0.01 #m
R = D / 2. #m
delPtrue = 250.0 * 1000.0 #Pa
mdoti = 0.3
mdotf = 0.35
mdot = 0
soln1 = 0
qpp = 200 *1000 #W/m2
P = 2 * np.pi * R

A = np.pi * (R)**2 

#print 'The pipe area is {} m2'.format(A)

# liquid sodium 1
rho = 805 #kg/m3
mu = 1.8 / 1000. #Pa*s
Cp = 1250 #J/kgK
K = 58.34 #W/mK


for mdot in np.linspace(mdoti, mdotf, 100000):
    vel = mdot / (rho * A)
    Re = (rho * vel * D) / mu
    f = (0.184 / (4. * Re**(0.2)))
    delP = 4 * f * (L/D) * 0.5 * rho * vel**2
    
    if (delP - delPtrue) < 1.0:
        if (delP - delPtrue) > -1.0:    
            soln1 = mdot
            Ret = Re

print 'The mdot of liquid sodium is {} kg/s'.format(soln1)

Pr1 = (mu * Cp) / K
Pe1 = Pr1 * Re
Nu1 = 7 + (0.025 * Pe1**(0.8))
h1 = (Nu1 * K) / D

Tmax1 = (qpp / h1) + ((qpp*P)/(soln1*Cp))*(L) + 600


print 'The maximum wall temperature for the liquid sodium is {} K'.format(Tmax1)




# molten salt 2
rho = 1960 #kg/m3
mu = 0.004087 #Pa*s
Cp = 2400 #J/kgK
K = 1.1 #W/mK

mdoti = 0.45
mdotf = 0.5
mdot = 0
soln2 = 0

for mdot in np.linspace(mdoti, mdotf, 100000):
    vel = mdot / (rho * A)
    Re = (rho * vel * D) / mu
    f = (0.184 / (4. * Re**(0.2)))
    delP = 4 * f * (L/D) * 0.5 * rho * vel**2
    
    if (delP - delPtrue) < 1.0:
        if (delP - delPtrue) > -1.0:    
            soln2 = mdot
            Ret = Re


print 'The mdot of molten salt is {} kg/s'.format(soln2)


Pr2 = (mu * Cp) / K
Pe2 = Pr2 * Re
Nu2 = 7 + (0.025 * Pe2**(0.8))
h2 = (Nu2 * K) / D


Tmax2 = (qpp / h2) + ((qpp*P)/(soln2*Cp))*(L) + 600


print 'The maximum wall temperature for the molten salt is {} K'.format(Tmax2)







###############################################################################
#                             PROBLEM 2
###############################################################################

D = 0.04 #m
R = 0.02 #m
mdot = 0.025 #kg/s
h = 1000 #W/m2K
qopp = 10000 #W/m2
L = 4 #m
Cp = 4180 # J/KgK
Ti = 25 #deg C
P = 2 * np.pi * R

zz = np.linspace(0, 4, 10000)

qpp = qopp * np.sin((np.pi * zz) / L)

Tc = ((P * qopp * L)/ (mdot * Cp * np.pi)) * (1.0 - np.cos((np.pi * zz) / L)) + Ti

Tw = (qpp / h) + Tc

print 'The fluid outlet temperature is {} deg C'.format(max(Tc))
print 'The max wall temperature is {} deg C'.format(max(Tw))

z = 3.27
qppt = qopp * np.sin((np.pi * z) / L)
Tct = ((P * qopp * L)/ (mdot * Cp * np.pi)) * (1.0 - np.cos((np.pi * z) / L)) + Ti
Twt = (qppt / h) + Tct

print 'The value of Tw at {} is {}'.format(z, Twt)

plt.figure()
plt.title("Comparison of Wall and Coolant Temperatures")
plt.xlabel("Length (m)")
plt.ylabel("Temp (deg C)")
plt.axis([0, 4, 0, 100])
plt.plot(zz, Tc, label='Coolant Temperature', color = 'k')
plt.plot(zz, Tw, label='Wall Temperature', color = 'g')
plt.legend()
plt.savefig('hw3p2.png')















