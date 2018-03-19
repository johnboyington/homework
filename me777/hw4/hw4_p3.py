
'''
me777 hw4 p3; book problem 6-3
'''

import numpy as np
import matplotlib.pyplot as plt
from numpy import sqrt, log, exp, pi
from numpy.random import rand
from scipy.stats import norm
from scipy.integrate import nquad
from time import time
from mpl_toolkits.mplot3d import Axes3D


class Hw4_P3(object):
    def __init__(self, rerun=False):
        print('PROBLEM 3')
        self.setup()
        if rerun:
            self.total_time = time()
            self.I, self.err = self.cycle(self.n)
            self.save_data()
            self.total_time = time() - self.total_time
            print('Time (s):  {}'.format(self.total_time))
        self.load_data()
        print(self.I)
        print(self.err)
        print('\n')

    def setup(self):
        self.mu = 1
        self.sig = 0.4
        self.n = int(1E5)
        self.x1 = 5
        self.y1 = 0.25
        self.z1 = 1
        self.x_i = self.x1
        self.y_i = self.y1
        self.z_i = self.z1
        self.u_i = None
        self.I = None
        self.err = None
        self.normal = norm(loc=self.mu, scale=self.sig)

    def F(self, x, y, z):
        return self.z(x, y, z) * self.f(x) * self.g(y) * self.h(z)

    def f(self, x):
        return (4/9) - (x/18)

    def g(self, y):
        return 4 * exp(-4 * y)

    def h(self, z):
        return self.normal.pdf(z)

    def f_prop(self, x):
        return 1/6

    def g_prop(self, y):
        return 4 * exp(-4 * y)

    def h_prop(self, z):
        return self.normal.pdf(z)

    def F_inv(self, rho):
        return 2 + rho * 6

    def G_inv(self, rho):
        return -log(rho) / 4

    def H_inv(self, rho):
        return self.normal.ppf(rho)

    def z(self, x, y, z):
        return (x / y)**z

    def sample(self):
        u_i = self.F_inv(rand())
        v_i = self.G_inv(rand())
        w_i = self.H_inv(rand())
        top_l = self.f(u_i) * self.g(v_i) * self.h(w_i)
        top_r = self.f_prop(self.x_i) * self.g_prop(self.y_i) * self.h_prop(self.z_i)
        top = (top_l * top_r)
        bot_l = self.f(self.x_i) * self.g(self.y_i) * self.h(self.z_i)
        bot_r = self.f_prop(u_i) * self.g_prop(v_i) * self.h_prop(w_i)
        bot = (bot_l * bot_r)
        R = top / bot
        alpha = min([1, R])
        if rand() <= alpha:
            self.x_i, self.y_i, self.z_i = u_i, v_i, w_i
        else:
            self.x_i, self.y_i, self.z_i = self.x_i, self.y_i, self.z_i

    def cycle(self, N):
        s = 0
        s2 = 0
        for i in range(N):
            self.sample()
            v = self.z(self.x_i, self.y_i, self.z_i)
            s += v
            s2 += v**2
        I_N = s / N
        err = ((s2 / N) - I_N**2) * (N / (N - 1))
        err = sqrt(err / N)  # std dev of the sample mean
        return I_N, err

    def save_data(self):
        with open('hw4_p3.txt', 'w+') as F:
            F.write('{}  {}\n'.format(self.I, self.err))

    def load_data(self):
        self.data = np.loadtxt('hw4_p3.txt')
        self.I, self.err = self.data


if __name__ == '__main__':
    Hw4_P3()
