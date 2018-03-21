
'''
me777 hw4 p2; book problem 6-2
'''

import numpy as np
import matplotlib.pyplot as plt
from numpy import sqrt, log, exp
from numpy.random import rand
from scipy.stats import multivariate_normal as mv
from time import time


class Hw4_P2(object):
    def __init__(self, rerun=False):
        print('PROBLEM 2')
        if rerun:
            self.total_time = time()
            self.setup()
            self.I, self.err = self.cycle(self.n)
            self.save_data()
            self.total_time = time() - self.total_time
            print('Time (s):  {}'.format(self.total_time))
        self.load_data()
        print(self.I)
        print(self.err)
        print('\n')

    def setup(self):
        self.mu1 = 5
        self.mu2 = 1
        self.sig1 = 1
        self.sig2 = 0.5
        self.sig12 = 0.25
        self.n = int(1E5)
        self.x1 = 4.8
        self.x_i = self.x1
        self.y1 = 1.2
        self.y_i = self.y1
        self.u_i = None
        self.I = None
        self.err = None

    def F(self, x):
        return x**2 * self.beta.pdf(x)

    def f(self, x, y):
        self.bivariate = mv([self.mu1, self.mu2], [[self.sig1**2, self.sig12], [self.sig12, self.sig2**2]])
        return self.bivariate.pdf((x, y))

    def g(self, u):
        return 2 * exp(-4 * abs(u))

    def h(self, v):
        return 0.25 * exp(0.5 * abs(v))

    def G_inv(self, rho):
        if rho >= 0.5:
            rho -= 0.5
            return -log(1 - 2*rho) / 4
        else:
            return log(2*rho) / 4

    def H_inv(self, rho):
        if rho >= 0.5:
            rho -= 0.5
            return -log(1 - 2*rho) / 0.5
        else:
            return log(2*rho) / 0.5

    def z(self, x, y):
        return x + y

    def sample(self):
        u_i = self.G_inv(rand())
        v_i = self.H_inv(rand())
        R = (self.f(u_i, v_i) * self.g(self.x_i) * self.h(self.y_i)) / (self.f(self.x_i, self.y_i) * self.g(u_i) * self.h(v_i))
        alpha = min([1, R])
        if rand() <= alpha:
            self.x_i = u_i
        else:
            self.x_i = self.x_i

    def cycle(self, N):
        s = 0
        s2 = 0
        for i in range(N):
            self.sample()
            v = self.z(self.x_i, self.y_i)
            s += v
            s2 += v**2
        I_N = s / N
        err = ((s2 / N) - I_N**2) * (N / (N - 1))
        err = sqrt(err)
        return I_N, err

    def save_data(self):
        with open('hw4_p2.txt', 'w+') as F:
            F.write('{}  {}\n'.format(self.I, self.err))

    def load_data(self):
        self.data = np.loadtxt('hw4_p2.txt')
        self.I, self.err = self.data


if __name__ == '__main__':
    Hw4_P2(True)
