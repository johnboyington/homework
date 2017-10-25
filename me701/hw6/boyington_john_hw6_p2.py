from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

alpha = 1

def getTemp(alpha, L=1, tMax=0.1):
    dt = 0.00005
    dx = 0.01
    Nx = int(L / dx)
    dx = L / Nx
    Nt = int(tMax / dt)
    dt = tMax / Nt

    dx = L / Nx
    dt = tMax / Nt

    assert dt * alpha / dx ** 2 <= 0.5, 'Parameters are not numerically stable'

    temp = np.zeros(Nx)
    temp[0] = 1

    for i in range(Nt):
        temp[1:-1] += dt * alpha / dx ** 2 * (temp[0:-2] - 2 * temp[1:-1] + temp[2:])
    return temp, np.linspace(0, L, Nx)





def live_animation():
    # number particles
    n = 1000
    # initialize particle positions
    # set up live
    plt.ion()
    plt.show()
    alphas = np.linspace(0, 1, 100)
    for a in alphas:
        plt.figure(1)
        plt.clf()
        T, x = getTemp(a)
        plt.plot(x, T)
        plt.title('alpha = {}'.format(a))
        plt.axis([0, 1, 0, 1])
        plt.draw()
        plt.pause(0.02)
   

live_animation()
