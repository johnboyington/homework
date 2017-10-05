
###############################################################################
#                                Homework 4
###############################################################################

import re
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# TODO: comment everything
# TODO: talk to Roberts about p3
# TODO: mention 0.5 norm, etc.


###############################################################################
#                                PROBLEM 1
###############################################################################

goodString = 'pit spot spate slap two respite '
badString = 'pt Pot peat part '
badList = badString.split()
goodList = goodString.split()[:3] + ['slap two'] + goodString.split()[-1:]

totString = goodString + badString

s = r'[a-z]*p[\s\S]t[a-z]*'
p = re.compile(s)
found = p.findall(totString)

print(sorted(found) == sorted(goodList))


###############################################################################
#                                PROBLEM 2
###############################################################################

with open('regex_sample_mcnp.txt', 'r') as f:
    mcnpOutput = f.read()

s = r'1tally'
tallyLocator = re.compile(s)
tallyIndx = tallyLocator.finditer(mcnpOutput)
indx = []
for match in tallyIndx:
    indx.append(match.span()[1])


s = r'\d.\d\d\d\dE[+-]\d\d   \d.\d\d\d\d\dE[+-]\d\d \d.\d\d\d\d'
dataPtrn = re.compile(s)

keys = [18, 28]
d = {keys[0]: {'energy': [], 'value': [], 'sigma': []}, keys[1]: {'energy': [], 'value': [], 'sigma': []}}
for i in range(len(keys)):
    data = dataPtrn.finditer(mcnpOutput[indx[i]:indx[i + 1]])
    for datum in data:
        dataStr = datum.group().split()
        d[keys[i]]['energy'].append(float(dataStr[0]))
        d[keys[i]]['value'].append(float(dataStr[1]))
        d[keys[i]]['sigma'].append(float(dataStr[2]))

checkDict = {18: {'energy': [0.0000E+00, 3.0000E-01, 2.0000E+02],
                  'value': [0.00000E+00, 0.00000E+00, 3.35200E-01],
                  'sigma': [0.0000, 0.0000, 0.0141]},
             28: {'energy': [0.0000E+00, 3.0000E-01, 2.0000E+02],
                  'value': [0.00000E+00, 7.00000E-04, 9.99300E-01],
                  'sigma': [0.0000, 0.3778, 0.0003]}}

print(d == checkDict)


###############################################################################
#                                PROBLEM 3
###############################################################################

# hard code bonner sphere data
sphDia = np.array([0.0, 2.0, 3.0, 5.0, 8.0, 10.0, 12.0])
resData = np.array([141585, 102435, 76796, 38056, 13923, 8091, 4834])


def fun(params, x, y, norm):
    a, b = params
    y_approx = a * sp.exp(-x * b)
    return np.linalg.norm(y - y_approx, ord=norm)


sol = sp.optimize.minimize(fun, x0=[160000, 0.01], args=(sphDia, resData, 2))
a, b, = sol.x
sol2 = sp.optimize.minimize(fun, x0=[160000, 0.1], args=(sphDia, resData, np.inf))
a2, b2 = sol2.x
xFine = np.linspace(0, 12, 100)
y_approx1 = a * sp.exp(-xFine * b)
y_approx2 = a2 * sp.exp(-xFine * b2)


plt.figure(0)
plt.plot(sphDia, resData, 'ro', label='Bonner Sphere Response Data')
plt.plot(xFine, y_approx1, 'b:', label='Least-Squares Fit')
plt.plot(xFine, y_approx2, 'g:', label='Minimax Fit')
plt.xlabel('Sphere Diameter $cm$')
plt.ylabel('Response $counts$')
plt.legend()
plt.show()
plt.close()


###############################################################################
#                                PROBLEM 4
###############################################################################

#from scipy.integrate import odeint
#def rhs(y, t, a):
#    return -a*y[0]
#times = sp.linspace(0, 10)
#sol = odeint(rhs, [1], times, args=(2,)) # notice that (2,) is needed to make it appears as a tuple.
#sol = sol.reshape((len(times))) # returns an array of array (one array per time step with each unknown)
#plt.plot(times, sol)
#plt.xlabel('t')
#plt.ylabel('y(t)')
#plt.show()


times = sp.linspace(0, 10, 100)

# 1
def rhs1(y, t):
    return y + 1

sol1 = odeint(rhs1, [1], times)

plt.figure(1)
plt.plot(times, sol1)
plt.title('Equation 1')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()
plt.close()



#def rhs(u, t, a, b): # using u.  remember, function argument names are arbitrary
#    y, z = u # unpack
#    dydt = -a*y
#    dzdt = -b*z + a*y
#    return dydt, dzdt
#times = sp.linspace(0, 10)
#sol = odeint(rhs, [1, 0], times, args=(1, 1)) # notice that (2,) is needed to make it appears as a tuple.
#sol = sol.T
#plt.plot(times, sol[0], 'k-', label='y(t)')
#plt.plot(times, sol[1], 'r--', label='z(t)')
#plt.xlabel('t')
#plt.legend()
#plt.show()

# 2
#def rhs2(args, t):
#    y, z, a = args
#    return z, a, y - z
#
#sol2 = odeint(rhs2, [1, 1, 1], times)
#
#
#
#plt.figure(2)
#plt.plot(times, sol2)
#plt.title('Equation 2')
#plt.xlabel('t')
#plt.ylabel('y(t)')
#plt.show()
#plt.close()


# 3
def rhs3(args, t, a, b):
    y, z = args
    dydt = (a * y) + 1
    dzdt = (b * z) + (a * y)
    return dydt, dzdt

sol3 = odeint(rhs3, [1, 1], times, args=(1000, 0.0001)).T

plt.figure(3)
plt.plot(times, sol3[0], label="y'")
plt.plot(times, sol3[1], label="z'")
plt.title('Equation 3')
plt.xlabel('t')
plt.ylabel('y(t)')
#plt.yscale('log')
plt.legend()
plt.show()
plt.close()



# 4
def rhs4(y, t):
    return y**2 + 1
times = np.linspace(0, 10, 300)
sol4 = odeint(rhs1, [1], times)

myY = [1]


for i in range(len(times)-1):
    step = (myY[i]**2 + 1) * (times[i + 1] - times[i]) + myY[i]
    myY.append(step)


myY2 = [1]
myY3 = [1]
delT = times[1] - times[0]

a = delT
b = -1

for i in range(len(times)-1):
    c = -(myY2[i] + delT)
    root0 = (-b + np.sqrt(b**2 - (4 * a * c))) / (2 * a)
    root1 = (-b - np.sqrt(b**2 - (4 * a * c))) / (2 * a)
    myY2.append(root0)
    
    c = -(myY3[i] + delT)
    root0 = (-b + np.sqrt(b**2 - (4 * a * c))) / (2 * a)
    root1 = (-b - np.sqrt(b**2 - (4 * a * c))) / (2 * a)
    myY3.append(root1)




plt.figure(4)
plt.plot(times, sol4, label='Using odeint')
plt.plot(times, myY, label="Forward Euler")
plt.plot(times, myY2, label="Backwards Euler (root 1)")
plt.plot(times, myY2, label="Backwards Euler (root 2)")
plt.title('Equation 4')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.yscale('log')
plt.xlim(0, 10)
plt.ylim(10**0, 10**5)
plt.legend()
#plt.savefig('me701_hw4_p4_4.png')
plt.show()
plt.close()





















