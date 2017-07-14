#ne737 hw4

import numpy as np
import matplotlib.pyplot as plt

###############################################################################
#                             PROBLEM 2
###############################################################################

def ZETA(SS, RR, oSS, oRR):
    top = (SS - RR)**2
    bot = oSS**2 + oRR**2
    return top / bot


S1 = np.loadtxt('temp1.txt')
S2 = np.loadtxt('temp2.txt')
R = np.loadtxt('response.txt')
v = 9.0
oS1 = np.sqrt(S1)
oS2 = np.sqrt(S2)
oR = np.sqrt(R)
W = [-1, 0, 1]


T1 = []
T2 = []

for i in (np.array(range(len(S1)-2))+1):
    for j in (np.array(range(len(S1)-2))+1):
        S = 0
        for a in W:
            for b in W:
                Z =  ZETA(S1[i+a, j+b], S2[i+a, j+b], oS1[i+a, j+b], oS2[i+a, j+b])
                S += Z
        T1.append(S)

T1 = (np.array(T1) / v).reshape(8,8)


for i in (np.array(range(len(S1)-2))+1):
    for j in (np.array(range(len(S1)-2))+1):
        S = 0
        for a in W:
            for b in W:
                Z =  ZETA(S1[i+a, j+b], R[i+a, j+b], oS1[i+a, j+b], oR[i+a, j+b])
                S += Z
        T2.append(S)

T2 = (np.array(T2) / v).reshape(8,8)

plt.figure(0)
plt.imshow(T1, cmap='Greys', vmin=0, vmax=np.max(T2))
plt.savefig('p2a.png')

plt.figure(1)
plt.imshow(T2, cmap='Greys', vmin=0, vmax=np.max(T2))
plt.savefig('p2b.png')

print T2