'''
me777 homework 1 problem 1; book problem 1-2
'''
import numpy as np


def u(x):
    return 6 * x - 1


def f(x):
    assert x >= 0 and x <= 1, 'Number out of bounds'
    return 1


# (a)
# What is the expected value of u with respect to this pdf?

mean_value = 2  # found analytically


# (b)
# Use these pseudorandom numbers to estimate the mean.

pseudo = np.array([0.985432, 0.509183, 0.054991, 0.641903, 0.390188, 0.719905, 0.876302, 0.251175, 0.160938, 0.487301])

s = 0
for x in pseudo:
    s += u(x)

mc_mean = (1 / len(pseudo)) * s

e = 0
for x in pseudo:
    e += (u(x) - mc_mean)**2
err = np.sqrt(e / (len(pseudo) - 1))

print('The mean value is:  {} +- {}'.format(mc_mean, err))
