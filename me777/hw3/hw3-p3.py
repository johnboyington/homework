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
    err = (N/(N - 1))*((s2 / N) - (val / N)**2)
    return val, err


def strat(N1, N2, N3, N4, area):
    quads = [0, 0, 0, 0]
    N_tot = N1 + N2 + N3 + N4
    Ns = [N1, N2, N3, N4]
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
    for i, q in enumerate(quads):
        pm = (Ns[i] / N_tot)
        v, er = q
        s += pm * v
        e += (pm * er) / N_tot
    return s * area, e * area


def whole(N, area):
    s, e = sample_mean(F, N, -5, 5, -5, 5)
    e = e / N
    return s * area, e * area

###############################################################################
#                             simple experiemnt
###############################################################################

if False:
    a = 10 * 10
    sm = []
    st = []

    n_values = np.logspace(3, 5, 10)
    l = 0

    for n in n_values:
        d1 = 0.6
        d2 = d3 = d4 = (1 - d1) / 3
        st.append(strat(int(d1*n), int(d2*n), int(d3*n), int(d4*n), a)[l])

        sm.append(whole(int(n), a)[l])

    fig = plt.figure(0)
    ax = fig.add_subplot(111)
    ax.plot(n_values, st, label='Stratified Sampling')
    ax.plot(n_values, sm, label='Sample Mean')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.legend()

###############################################################################
#                             main experiemnt
###############################################################################
if True:
    a = 10 * 10
    sm = []
    st0 = []
    st1 = []
    st2 = []
    st3 = []

    n_values = np.logspace(2, 5, 30)
    l = 1

    for n in n_values:
        d1, d2, d3, d4 = 0.25, 0.25, 0.25, 0.25
        st0.append(strat(int(d1*n), int(d2*n), int(d3*n), int(d4*n), a)[l])

        d1, d2, d3, d4 = 0.4, 0.2, 0.2, 0.2
        st1.append(strat(int(d1*n), int(d2*n), int(d3*n), int(d4*n), a)[l])

        d1, d2, d3, d4 = 0.1, 0.3, 0.3, 0.3
        st2.append(strat(int(d1*n), int(d2*n), int(d3*n), int(d4*n), a)[l])


        sm.append(whole(int(n), a)[l])

    fig = plt.figure(0)
    ax = fig.add_subplot(111)
    for s in [sm, st0, st1, st2]:
        ax.plot(n_values, s)
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('N')
    ax.set_ylabel('$\sigma^2$')
    ax.legend(['Sample Mean', '$p_1 = 0.25$', '$p_1 = 0.15$', '$p_1 = 0.625$'])

#############################################################################
#                       plotting 3d
#############################################################################
plot = True
if plot:
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    # create x and y points for 3d plotting
    xx, yy = np.meshgrid(x, y)
    fig = plt.figure(99)
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
