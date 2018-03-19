'''
me777 hw4 p1; book problem 6-1
'''

import numpy as np
import matplotlib.pyplot as plt
from numpy import sqrt
from numpy.random import rand
from scipy.stats import beta
from time import time


class Hw4_P1(object):
    def __init__(self, rerun=False):
        print('PROBLEM 1')
        if rerun:
            self.total_time = time()
            self.setup()
            self.burn_all()
            self.save_data()
            self.total_time = time() - self.total_time
            print('Time (s):  {}'.format(self.total_time))
        self.load_data()
        print(self.I)
        print(self.err)
        print('\n')

    def setup(self):
        self.a = 1.5
        self.b = 1.2
        self.n = int(1E5)
        self.x1 = 0.5
        self.burnin_lengths = [int(0), int(1E3), int(1E4)]
        self.beta = beta(self.a, self.b)
        self.x_i = self.x1
        self.u_i = None
        self.I = None
        self.err = None

    def F(self, x):
        return x**2 * self.beta.pdf(x)

    def f(self, x):
        return self.beta.pdf(x)

    def sample(self):
        u_i = rand()
        R = self.f(u_i) / self.f(self.x_i)
        alpha = min([1, R])
        if rand() <= alpha:
            self.x_i = u_i
        else:
            self.x_i = self.x_i

    def cycle(self, N, m):
        s = 0
        s2 = 0
        for i in range(N+m):
            self.sample()
            if i >= m:
                v = self.x_i**2
                s += v
                s2 += v**2
        I_N = s / N
        err = ((s2 / N) - I_N**2) * (N / (N - 1))
        err = sqrt(err)
        return I_N, err

    def burn_all(self):
        self.I = []
        self.err = []
        for m in self.burnin_lengths:
            print('Burning: {}'.format(m))
            I, e = self.cycle(self.n, m)
            self.I.append(I)
            self.err.append(e)

    def save_data(self):
        with open('hw4_p1.txt', 'w+') as F:
            for v, e in zip(self.I, self.err):
                F.write('{}  {}\n'.format(v, e))

    def load_data(self):
        self.data = np.loadtxt('hw4_p1.txt')
        self.data = self.data.T
        self.I, self.err = self.data


if __name__ == '__main__':
    Hw4_P1()
