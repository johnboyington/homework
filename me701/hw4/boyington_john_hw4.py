###############################################################################
#                                Homework 4
###############################################################################

import re
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# TODO: comment everything
# TODO: talk to Roberts about p3


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

M = np.array([sphDia, np.ones(len(sphDia))]).T

z = np.linalg.lstsq(M, resData)[0]
y_approx = M.dot(z)


def fun(params, x, y):
    a, b = params
    y_approx = a * sp.exp(-x * b)
    err = y - y_approx
    return sum(abs(err))


sol = sp.optimize.minimize(fun, x0=[160000, 0.1], args=(sphDia, resData))
a2, b2 = sol.x
xFine = np.linspace(0, 12, 100)
y_approx2 = a2 * sp.exp(-xFine * b2)


plt.figure(0)
plt.plot(sphDia, resData, 'ro', label='Bonner Sphere Response Data')
plt.plot(xFine, y_approx2, 'g:', label='Exponential Fit')
plt.plot(sphDia, y_approx, 'b:', label='Linear Least Squares Fit')
plt.xlabel('Sphere Diameter $cm$')
plt.ylabel('Response $counts$')
plt.legend()


###############################################################################
#                                PROBLEM 4
###############################################################################

# 1
































