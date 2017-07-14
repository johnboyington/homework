#this code will help plot some stuff from my hw 6 ne620

import numpy as np
import matplotlib.pyplot as plt

temp = np.loadtxt('data_temp.txt')
chf_out = np.loadtxt('data_chf.txt')
vel = np.loadtxt('data_vel.txt')
pr = np.loadtxt('data_pr.txt') * 0.000145038
apf = np.loadtxt('data_pf.txt').T[2]
z = np.array(range(30)) * (38.2 / 30)
Phot = 2.35294E4 #W
Dh = 0.0168 #m
DH = 0.0184 #m

#convert to english units for correlation
vele = vel * 3.28084 * 12 #m/s to ft/s to in/s
Dhe = Dh *  3.28084 * 12 #m to ft to in
DHe = DH *  3.28084 * 12 #m to ft to in

cfactor = 1.8991 #kJW in one Pcu/s


#Bernath correlation
DEL = 48 / (Dhe ** 0.6)
A = pr / (pr + 15)
B = vele / 4
C = A - B
Tbo = 57 * np.log(pr) - (54 * (C))
hbo = 10890 * (Dhe / (Dhe + DHe)) + (DEL * vele)
Qbo = (hbo * (Tbo - temp)) * cfactor
Qbo = Qbo * (1 / 3.28084)

#calc axial q
qp = apf * Phot * (1/DH)

#calc departure
DNBR = Qbo / qp


plt.figure(0)
plt.title("Triga CHF")
plt.xlabel("Axial Position (cm)")
plt.ylabel("Heat Flux ($Pcu/ft^2$)")
plt.xlim(1, 39)
plt.ylim(0, 2e5)
#plt.plot(z, chf_out, label='CHF from Output File')
plt.plot(z, Qbo, label='CHF from Correlation')
plt.plot(z, qp, label='Heat Flux')
plt.legend()
plt.savefig('TrigaCHF.png')

plt.figure(1)
plt.title("Departure from Nucleate Boiling Ratio")
plt.xlabel("Axial Position (cm)")
plt.ylabel("DNBR")
plt.xlim(1, 39)
plt.ylim(0, 6)
plt.plot(z, DNBR)
plt.savefig('DNBR.png')