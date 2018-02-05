'''
me777 homework 1 problem 3; book problem 1-5
'''
import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt


def pcut(theta, L, D):
    return (L / (np.pi * D)) * np.sin(theta)


x_l = 0
x_h = np.pi
x_diff = x_h - x_l


under = 0
total = 0

x_full = np.linspace(x_l, x_h, 1000)
fig = plt.figure(0)
ax = fig.add_subplot(111)
ax.plot(x_full, pcut(x_full, 1, 2))
ax.set_xlim(x_l, x_h)

s = 0
for i in range(2000):
    x = rand()
    x = x_l + (x_diff * x)
    y = pcut(x, 1, 2)
    s += y
    ax.plot(x, y, 'ko', color='k', ms=0.5)
    total += 1

integral = (s / total) * (x_diff)
pcut_true = 1 / np.pi
diff = integral - pcut_true

print('The value of the integral is:  {}'.format(integral))
print('The difference from the true value is:  {}'.format(diff))
