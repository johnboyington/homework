'''
me777 hw3 problem 2, book problem 4-6
'''
from numpy.random import rand
import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
from time import time


class Wedge_Tail(object):
    def __init__(self):
        self.k = 20
        self.delta = 0.5
        self.i = np.array(range(1, self.k + 1))
        self.x = np.array([0] + list(self.i * self.delta))
        self.calc_areas()

    def sample(self):
        rho = rand()
        self.j = 0
        for j, a in enumerate(self.areas):
            if rho > a:
                self.j = j + 1
            else:
                break

        # grab a new random number
        self.rho = rand()
        return float(self.cdfs())

    def calc_areas(self):
        A_i = self.delta * np.exp(-self.i * self.delta)
        A_k_plus_i = np.exp(-self.i * self.delta)*(np.exp(self.delta) - 1 - self.delta)
        A_2k_plus_i = np.exp(-self.k * self.delta)

        areas = []
        for A in A_i:
            areas.append(A)
        for A in A_k_plus_i:
            areas.append(A)
        for A in [A_2k_plus_i]:
            areas.append(A)

        total_area = sum(areas)
        areas = np.array(areas) / total_area
        self.areas = np.array(areas) / total_area
        for i, a in enumerate(self.areas):
            self.areas[i] = np.sum(areas[0:i+1])

    def cdfs(self):
        if self.j == len(self.areas):
            self.x_L = max(self.x)
            return fsolve(self.cdf3, 5)
        elif self.j >= len(self.areas[:-1]) / 2:
            self.x_L = self.x[self.j - len(self.x)]
            return fsolve(self.cdf2, 2)
        else:
            self.x_L = self.x[self.j]
            return self.rho * self.delta + self.x_L

    def cdf1(self, x):
        return ((1 / self.delta) * (x - self.x_L)) - self.rho

    def cdf2(self, x):
        A = np.exp(self.delta) - 1 - self.delta
        T1 = -np.exp(-x + self.i * self.delta) - x
        T2 = -np.exp(-self.x_L + self.i * self.delta) - self.x_L
        return ((1/A) * (T1 - T2)) - self.rho

    def cdf3(self, x):
        T1 = -np.exp(-x + self.k * self.delta)
        T2 = np.exp(-self.x_L + self.k * self.delta)
        return (T1 + T2) - self.rho

    def sample_icdf(self):
        rho = rand()
        return -np.log(rho)


WT = Wedge_Tail()

##########################################
#                 test
##########################################
if True:
    xs = WT.x
    scores = np.zeros(len(xs))
    for i in range(100000):
        s = WT.sample_icdf()
        for j in range(len(xs)-1):
            if s > xs[j] and s < xs[j+1]:
                scores[j] += 1
    scores = (scores / sum(scores)) * (1 / (xs[1] - xs[0]))

    x_vals = np.linspace(0, 10, 100)
    y_vals = np.exp(-x_vals)

#########################################
#             timing
#########################################
N_samples = 100000

t_rwt = time()
for i in range(N_samples):
    WT.sample()
t_rwt = time() - t_rwt

t_icdf = time()
for i in range(N_samples):
    WT.sample_icdf()
t_icdf = time() - t_icdf

print('\n')
print('Rectangle-Wedge-Tail Method:  {}'.format(t_rwt))
print('Inverse CDF Method:  {}'.format(t_icdf))
print('Ratio:  {}'.format(t_rwt / t_icdf))

#########################################
#             plotting
#########################################
fig = plt.figure(0)
ax = fig.add_subplot(111)
ax.step(xs, scores, 'k', where='post', label='Sampling')
ax.plot(x_vals, y_vals, 'g-.', label='$e^{-x}$')
ax.set_xlabel('x')
ax.set_ylabel('p(x)')
ax.set_yscale('log')
ax.legend()
