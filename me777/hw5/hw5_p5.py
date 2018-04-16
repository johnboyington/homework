import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt


def q(x):
    return 10 - x


def walk_on_lines(r, n, bounds, bound_temp, tol):
    s = 0
    for z in range(n):
        x = r
        qs = 0
        found = False
        while not found:
            L, R = abs(bounds[0] - x), abs(bounds[1] - x)
            if L < R:
                line = [bounds[0], x + L]
            else:
                line = [x - R, bounds[1]]
            x_old = x
            x = line[0] + rand()*(line[1] - line[0])
            qs += q(x) * (x_old**2) / 2
            if x - bounds[0] < tol:
                s += bound_temp[0] + qs
                found = True
            elif bounds[1] - x < tol:
                s += bound_temp[1] + qs
                found = True
    return s / n


xs = np.linspace(0, 10, 50)
t = [[], [], [], []]
for x in xs:
    # t[0].append(walk_on_lines(x, 10000, [0, 10], [10, 50], 0.1))
    t[1].append(walk_on_lines(x, 1000, [0, 10], [10, 50], 0.1))
    # t[2].append(walk_on_lines(x, 100, [0, 10], [10, 50], 0.1))
    # t[3].append(walk_on_lines(x, 10, [0, 10], [10, 50], 0.1))


fig = plt.figure(0)
ax = fig.add_subplot(111)
# ax.plot(xs, t[3], color='orange', linestyle=':', label='10 histories')
# ax.plot(xs, t[2], color='indigo', linestyle='-.', label='100 histories')
ax.plot(xs, t[1], color='green', linestyle='--', label='1000 histories')
# ax.plot(xs, t[0], color='red', linestyle='-', label='10000 histories')
ax.set_xlabel('x')
ax.set_ylabel('u(x)')
ax.legend()
plt.savefig('p5_2.png', dpi=300)
