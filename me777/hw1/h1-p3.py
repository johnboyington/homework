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

y_l = 0
y_h = 0.175
y_diff = y_h - y_l

under = 0
total = 0

x_full = np.linspace(x_l, x_h, 1000)
fig = plt.figure(0)
ax = fig.add_subplot(111)
ax.plot(x_full, pcut(x_full, 1, 2))
ax.set_xlim(x_l, x_h)
ax.set_ylim(y_l, y_h)

for i in range(5000):
    x, y = rand(), rand()
    x = x * x_diff + x_l
    y = y * y_diff + y_l
    y_true = pcut(x, 1, 2)
    if y < y_true:
        c = 'r'
        under += 1
    else:
        c = 'indigo'
    ax.plot(x, y, 'ko', color=c, ms=0.5)
    total += 1

integral = (under / total) * (x_diff * y_diff)

print('The value of the integral is:  {}'.format(integral))
