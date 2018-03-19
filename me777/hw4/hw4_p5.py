
'''
me777 hw4 p5; book problem 6-5
'''

import numpy as np
from numpy import sqrt, log, exp, pi, cos
from numpy.random import rand, randint
from time import time


class Hw4_P5(object):
    def __init__(self, rerun=False):
        print('PROBLEM 5')
        if rerun:
            self.total_time = time()
            self.setup()
            self.I0, self.err0 = self.cycle(self.n, 0)
            self.I1, self.err1 = self.cycle(self.n, 1)
            self.I2, self.err2 = self.cycle(self.n, 2)
            self.I = [self.I0, self.I1, self.I2]
            self.err = [self.err0, self.err1, self.err2]
            self.save_data()
            self.total_time = time() - self.total_time
            print('Time (s):  {}'.format(self.total_time))
        self.load_data()
        print(self.I)
        print(self.err)
        print('\n')

    def setup(self):
        self.n = int(1E6)
        self.x1 = 5
        self.y1 = 5
        self.z1 = 5
        self.x_i = self.x1
        self.y_i = self.y1
        self.z_i = self.z1
        self.u_i = None
        self.I = None
        self.err = None

    def F(self, x, y, z):
        return self.z(x, y, z) * self.f(x) * self.g(y) * self.h(z)

    def f(self, x):
        return 4 * exp(-4 * x)

    def g(self, y):
        return (3/150) * y

    def h(self, z):
        return 1 / (2 * sqrt(z))

    def f_prop(self, u):
        return 3 * exp(-3 * u)

    def g_prop(self, v):
        return 1/10

    def h_prop(self, w):
        return 2 * w

    def F_inv(self, rho):
        return -log(rho) / 3

    def G_inv(self, rho):
        return 10 * rho

    def H_inv(self, rho):
        return sqrt(rho)

    def z(self, x, y, z):
        return (300 / 4) * cos(x * y)

    def sample(self, case):
        # successively
        self.successivly = 0
        if case == 0:
            if self.successivly % 3 == 0:
                u_i = self.F_inv(rand())
                v_i = self.y_i
                w_i = self.z_i
            elif self.successivly % 3 == 1:
                u_i = self.x_i
                v_i = self.G_inv(rand())
                w_i = self.z_i
            else:
                u_i = self.x_i
                v_i = self.y_i
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
            self.successivly += 1
        # randomly
        if case == 1:
            rand_choice = randint(0, 3)
            if rand_choice == 0:
                u_i = self.F_inv(rand())
                v_i = self.y_i
                w_i = self.z_i
            elif rand_choice == 1:
                u_i = self.x_i
                v_i = self.G_inv(rand())
                w_i = self.z_i
            else:
                u_i = self.x_i
                v_i = self.y_i
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
        # globally
        if case == 2:
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

    def cycle(self, N, choice):
        s = 0
        s2 = 0
        for i in range(N):
            self.sample(choice)
            v = self.z(self.x_i, self.y_i, self.z_i)
            s += v
            s2 += v**2
        I_N = s / N
        err = ((s2 / N) - I_N**2) * (N / (N - 1))
        err = sqrt(err / N)  # std dev of the sample mean
        return I_N, err

    def save_data(self):
        with open('hw4_p5.txt', 'w+') as F:
            for v, e in zip(self.I, self.err):
                F.write('{}  {}\n'.format(v, e))

    def load_data(self):
        self.data = np.loadtxt('hw4_p5.txt')
        self.data = self.data.T
        self.I, self.err = self.data


if __name__ == '__main__':
    Hw4_P5()
