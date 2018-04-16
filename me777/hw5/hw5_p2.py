import numpy as np
from numpy import sqrt
from numpy.random import rand

y1 = 1
y2 = 3


def F(y):
    n = 1000000
    s = 0
    for i in range(n):
        s += rand()*y
    return s/n

xy1 = F(y1)
xy2 = F(y2)

A = np.array([[1, xy1], [1, xy2]])
R = np.array([2, 5])
theta = np.linalg.solve(A, R)
print(theta)
