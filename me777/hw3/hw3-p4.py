'''
me777 hw3 problem 1, book problem 5-3
'''
import numpy as np
import matplotlib.pyplot as plt


def x(rho):
    return 1 * rho + 1


def x_prime(rho):
    return 1 * (1 - rho) + 1


xs = []
xps = []
for i in np.linspace(0, 1, 100):
    xs.append(x(i))
    xps.append(x_prime(i))

plt.figure(0)
plt.plot(xs, xps)
plt.xlabel('$x$')
plt.ylabel("$x'$")
