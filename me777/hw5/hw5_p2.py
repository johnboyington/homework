import numpy as np
from numpy import sqrt
from numpy.random import rand

n = int(1E7)
a, b = 0, 1
dif = b - a
rho = rand()
R = np.array([2.0, 5.0])
Y = [1.0, 3.0]
A = np.ones((2, 2))

for i, y in enumerate(Y):
    s = 0
    s2 = 0
    for z in range(1, n+1):
        f = dif * rand() + a
        s += f
        s2 += f**2
    avg = (s / 2) * dif
    std2 = abs((s2 / n) - avg) / (n - 1)
    sig = sqrt(std2)
    A[i, 1] = avg * y

theta = np.linalg.solve(A, R)
print(theta)