'''
me777 hw3 problem 5, book problem 5-5
'''
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import rand


def g(x):
    return x ** 4


def sample_mean(f, N, a, b, true):
    s = 0
    for i in range(N):
        rho = rand()*(b - a) + a
        s += f(rho)
    val = (s * (b - a)) / N
    err = abs(val - true)
    return val, err


def antithetic(f, N, a, b, true):
    s = 0
    for i in range(N):
        rho = rand()
        r1 = rho * (b - a) + a
        r2 = (1 - rho) * (b - a) + a
        s += (f(r1) + f(r2))
    val = (s * (b - a)) / (2 * N)
    err = abs(val - true)
    return val, err


original = []
anti = []

Ns = np.logspace(1, 5, 30)
for n in Ns:
    original.append(sample_mean(g, int(n), 1, 3, 242/5)[1])
    anti.append(antithetic(g, int(n), 1, 3, 242/5)[1])

plt.figure(0)
plt.plot(Ns, original, 'k-', label='Sample Mean')
plt.plot(Ns, anti, 'g:', label='Antithetical')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('$N$')
plt.ylabel("$error$")
plt.legend()
