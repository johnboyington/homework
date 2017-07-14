#ne620 hw7 data analysis

import numpy as np
import matplotlib.pyplot as plt
import os

try:
    os.mkdir('output')
except OSError,e:
    print e


pres = np.arange(0.2, 7.7, 0.5) * 10**6
ie_l = np.array([504492, 696226, 796962, 869762, 928267, 977930, 1.022E6, 1.061E6, 1.096E6, 1.129E6, 1.6E6, 1.189E6, 1.217E6, 1.243E6, 1.269E6])
ie_v = np.array([2.529E6, 2.572E6, 2.588E6, 2.596E6, 2.601E6, 2.603E6, 2.603E6, 2.603E6, 2.601E6, 2.599E6, 2.596E6, 2.592E6, 2.588E6, 2.584E6, 2.579E6])

#print '0031201 000 {} {} {}  0.0  0.0 20'.format(pres[0], ie_l[0], ie_v[0] * 0.01)


###############################################################################
#                           FILE CREATION
###############################################################################

def TOP():
    H = open('edtop.txt', 'r').read()
    return H

def BOT():
    H = open('edbot.txt', 'r').read()
    return H

for nn in range(len(pres)):
    s = ''
    s += TOP()
    s += '0031201 000 {} {} {}  0.0  0.0 20\n'.format(pres[nn], ie_l[nn], ie_v[nn] * 0.01)
    s += BOT()
    with open('output/ed{}.i'.format(nn), 'w') as H:
                H.write(s)


def Extract(name):
    F = open('output/ed{}.o'.format(name), 'r').readlines()
    for ii in range(len(F)):
        if '1 time        p            p            p            p            p            voidg        voidj        mflowj' in F[ii]:
            line = np.array(F[ii + 4:ii + 54])
            data = np.loadtxt(line)
            return data.T
    return 


#plotting max discharge flowrate
plt.figure(0)
plt.title("Maximum Discharge Flow Rate as a function of Initial Pressure")
plt.xlabel("Pressure ($MPa$)")
plt.ylabel('Maximum Discharge Flow Rate ($kg/s$)')
plt.xlim(0, 8)
plt.ylim(0, 150)
y = []
for ii in range(len(pres)):
    y.append(np.max(Extract(ii)[8]))
plt.plot(pres * (10**(-6)), y, label='Max Flow', color='0.01')
plt.legend()
plt.savefig('flowrate.png')

#plotting void fraction behavior
plt.figure(1)
plt.rcParams['figure.figsize'] = [6.0, 5.0]
plt.title("Void Fraction Behavior with different initial pressures")
plt.xlabel("Time ($s$)")
plt.ylabel('Void Fraction')
plt.xlim(0, 0.42)
plt.ylim(0, 1)
t = Extract(0)[0]
for jj in range(len(pres)):
    y = Extract(jj)[7]
    plt.plot(t, y, label='{} $MPa$'.format(jj * 0.5 + 0.2), color='{}'.format((1 - (jj+1) * 0.066666)))
plt.legend(loc=4)
plt.savefig('void.png')


#plotting void fraction behavior
plt.figure(2)
plt.rcParams['figure.figsize'] = [6.0, 5.1]
plt.title("System Pressure Behavior with different initial pressures")
plt.xlabel("Time ($s$)")
plt.ylabel('Pressure ($MPa$)')
plt.xlim(0, 0.42)
plt.ylim(0, 7)
t = Extract(0)[0]
for jj in range(len(pres)):
    y = Extract(jj)[1] * 10**(-6)
    plt.plot(t, y, label='{} $MPa$'.format(jj * 0.5 + 0.2), color='{}'.format((1 - (jj+1) * 0.066666)))
plt.legend()
plt.savefig('ipressure.png')

#plotting void fraction behavior
plt.figure(3)
plt.rcParams['figure.figsize'] = [6.0, 5.1]
plt.title("Outlet Pressure Behavior with different initial pressures")
plt.xlabel("Time ($s$)")
plt.ylabel('Pressure ($MPa$)')
plt.xlim(0, 0.42)
plt.ylim(0, 7)
t = Extract(0)[0]
for jj in range(len(pres)):
    y = Extract(jj)[5] * 10**(-6)
    plt.plot(t, y, label='{} $MPa$'.format(jj * 0.5 + 0.2), color='{}'.format((1 - (jj+1) * 0.066666)))
plt.legend()
plt.savefig('opressure.png')
