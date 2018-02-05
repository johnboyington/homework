'''
me777 homework 1 problem 2; book problem 1-3
'''
import numpy as np
import matplotlib.pyplot as plt


def u(x):
    return np.exp(-x**2 / 2)


pseudo = np.array([0.985432, 0.509183, 0.054991, 0.641903, 0.390188, 0.719905, 0.876302, 0.251175, 0.160938, 0.487301])
x_l = -4
x_h = 4
x_diff = x_h - x_l

x_full = np.linspace(-4, 4, 100)
fig = plt.figure(0)
ax = fig.add_subplot(111)
ax.plot(x_full, u(x_full))

total = 0
s = 0
for x in pseudo:
    x = x_l + (x_diff * x)
    y = u(x)
    s += y
    ax.plot(x, y, 'ko', ms=3)
    total += 1

integral = (s / total) * (x_diff)

print('The value of the integral is:  {}'.format(integral))
