'''
me777 hw3 problem 3, book problem 5-2
'''
from numpy import sin
from numpy.random import rand
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def F(x, y):
    if x > 0 and y > 0:
        return x**2 * y**2 * sin(x)**2 * sin(y)**2
    else:
        return (x**2 * y**2) / 25


def sample_mean(f, N, ax, bx, ay, by):
    s = 0
    s2 = 0
    for i in range(N):
        rhox = rand()*(bx - ax) + ax
        rhoy = rand()*(by - ay) + ay
        s += f(rhox, rhoy)
        s2 += (f(rhox, rhoy))**2
    val = s / N
    err = ((s2 / N) - val**2) / N
    return val, err


def strat(N1, N2, N3, N4, area):
    quads = [0, 0, 0, 0]
    # sample quad I
    quads[0] = sample_mean(F, N1, 0, 5, 0, 5)
    # sample quad II
    quads[1] = sample_mean(F, N2, -5, 0, 0, 5)
    # sample quad III
    quads[2] = sample_mean(F, N3, -5, 0, -5, 0)
    # sample quad IV
    quads[3] = sample_mean(F, N4, 0, 5, -5, 0)
    s = 0
    e = 0
    for v, er in quads:
        s += 0.25 * v * area
        e += (0.25**2) * er * area
    return s, e


def whole(N, area):
    s, e = sample_mean(F, N, -5, 5, -5, 5)
    return s * area, e * area


a = 10 * 10
s = strat(1000, 1000, 1000, 1000, a)
w = whole(4000, a)

ntot = 50
nc = 0
for i in range(ntot):
    s = strat(1000, 1000, 1000, 1000, a)
    w = whole(4000, a)
    if s[1] > w[1]:
        nc += 1

print(nc / ntot)

plot = False
if plot:
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    # create x and y points for 3d plotting
    xx, yy = np.meshgrid(x, y)
    fig = plt.figure(0)
    ax = fig.add_subplot(111, projection='3d')
    # make surface plot
    F_xy = np.zeros((len(xx), len(yy)))
    for i, xxx in enumerate(xx):
        for j, yyy in enumerate(yy):
            F_xy[i, j] = F(xx[i, j], yy[i, j])
    ax.plot_surface(xx, yy, F_xy, cmap='plasma')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('F(x, y)')
    plt.show()
