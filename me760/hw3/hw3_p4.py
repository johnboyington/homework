
from numpy import sin, cos, pi, sqrt
import numpy as np
import matplotlib.pyplot as plt



###############################################################################
#                                me760 hw3 p2
###############################################################################

def r(u):
    i = cos(u)
    j = 2 * sin(u)
    return i, j

def tangent(l):
    i = 0.5 * (1 - l)
    j = sqrt(3) * (1 + (1/3) * l)
    return i, j

u_values = np.linspace(-2, 2, 1000)
l_values = np.linspace(-2, 2, 1000)
x1 = []
y1 = []
x2 = []
y2 = []
for u in u_values:
    x_val, y_val = r(u)
    x1.append(x_val)
    y1.append(y_val)

for l in l_values:
    x_val, y_val = tangent(l)
    x2.append(x_val)
    y2.append(y_val)

plt.figure(0)
plt.plot(x1, y1, label='curve')
plt.plot(x2, y2, label='tangent')
plt.plot(0.5, sqrt(3), 'ko', label='point P')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=1)
plt.savefig('p2.png')


###############################################################################
#                                me760 hw3 p4
###############################################################################



# this code produces a sketch of a cycloid


def cycloid(t, R=1, w=1):
    i = R * sin(w*t) + w*R*t
    j = R * cos(w*t) + R
    return i, j

times = np.linspace(0, 6*pi, 1000)
x = []
y = []
for t in times:
    x_val, y_val = cycloid(t)
    x.append(x_val)
    y.append(y_val)

plt.figure(1)
plt.plot(x, y, label='cycloid')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=1)
plt.savefig('cycloid.png')
