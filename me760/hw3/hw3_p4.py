###############################################################################
#                                me760 hw3 p4
###############################################################################

from numpy import sin, cos, pi
import numpy as np
import matplotlib.pyplot as plt


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

plt.figure(0)
plt.plot(x, y, label='cycloid')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=1)
plt.savefig('cycloid.png')
