import numpy as np
from numpy.random import rand
from numpy import cos, exp, log
import matplotlib.pyplot as plt


def f(x):
    return x**2 * cos(x) * exp(-(x/2))


s = 0
s2 = 0
N = 100000
for i in range(N):
    rho = rand()
    rho *= 30
    f_rho = f(rho)
    s += f(rho)
    s2 += f_rho**2
I = (30*s) / N
print(I)


x = np.linspace(0, 30, 1000)
plt.figure(0)
plt.plot(x, f(x))
plt.xlabel('x')
plt.ylabel('f(x)')