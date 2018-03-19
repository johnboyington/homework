
'''
me777 hw4 p2; book problem 6-2
'''

import numpy as np
import matplotlib.pyplot as plt
from numpy import sqrt, log, exp
from numpy.random import rand
from scipy.stats import gamma
from time import time


class Hw4_P4(object):
    def __init__(self, rerun=False):
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

    def setup(self):
        self.a = 2
        self.b = 1
        self.y = 0.5
        self.n = int(1E5)
        self.x1 = 1
        self.x_i = self.x1
        self.u_i = None
        self.I = None
        self.err = None

    def F(self, x):
        return self.z(x) * self.f(x)

    def f(self, x):
        self.gamma = gamma(self.a)
        return (1 / (self.b * 2)) * ((x / self.a)**(self.a - 1)) * (exp(-x / self.b))

    def h(self, x):
        return self.y * exp(-self.y * x)

    def H_inv(self, rho):
        return -log(1 - rho) / self.y

    def z(self, x):
        return (x - self.a * self.b)**2

    def sample(self):
        u_i = self.H_inv(rand())
        R = (self.f(u_i) * self.h(self.x_i)) / (self.f(self.x_i) * self.h(u_i))
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
            v = self.z(self.x_i)
            s += v
            s2 += v**2
        I_N = s / N
        err = ((s2 / N) - I_N**2) * (N / (N - 1))
        err = sqrt(err / N)  # std dev of the sample mean
        return I_N, err

    def save_data(self):
        with open('hw4_p4.txt', 'w+') as F:
            F.write('{}  {}\n'.format(self.I, self.err))

    def load_data(self):
        self.data = np.loadtxt('hw4_p4.txt')
        self.I, self.err = self.data


Hw4_P4()
