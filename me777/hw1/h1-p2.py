'''
me777 homework 1 problem 2; book problem 1-3
'''
import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt


def u(x):
    return np.exp(-x**2 / 2)


pseudo = np.array([0.985432, 0.509183, 0.054991, 0.641903, 0.390188, 0.719905, 0.876302, 0.251175, 0.160938, 0.487301])
x_l = -4
x_h = 4
x_diff = x_h - x_l

y_l = 0
y_h = 1
y_diff = y_h - y_l

under = 0
total = 0

#for i in range(10000):
#    pseudo = np.append(pseudo, rand())


x_full = np.linspace(-4, 4, 100)
fig = plt.figure(0)
ax = fig.add_subplot(111)
ax.plot(x_full, u(x_full))

for i in range(len(pseudo))[::2]:
    x, y = pseudo[i], pseudo[i+1]
    x = x * x_diff + x_l
    y = y * y_diff + y_l
    ax.plot(x, y, 'ko', ms=3)
    y_true = u(x)
    if y < y_true:
        under += 1
    total += 1

integral = (under / total) * (x_diff * y_diff)

print('The value of the integral is:  {}'.format(integral))
