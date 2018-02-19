'''
me777 hw2 problem 4
'''
from numpy import pi, sqrt
from time import time


class RNG(object):
    def __init__(self, seed, a, m):
        self.x = seed
        self.a = a
        self.m = m

    def pm(self):
        self.x = (self.a * self.x) % self.m
        self.x = self.x
        return self.x / self.m


rng = RNG(1, 16807, (2**31) - 1)


# verify efficiency of first method
def alg_1(R=1):
    rho_i, rho_j = rng.pm(), rng.pm()
    x_i = R*(1 - 2*rho_i)
    y_j = R*(1 - 2*rho_j)
    if x_i**2 + y_j**2 < R**2:
        return True, x_i, y_j
    else:
        return False, x_i, y_j

good = 0
bad = 0
for i in range(50000):
    choice = alg_1()[0]
    if choice:
        good += 1
    else:
        bad += 1

efficiency = good / (good + bad)
print('The efficiency of the first algorithm is:  {}'.format(efficiency))
print('Compare this with the analytical solution:  {}'.format(pi / 4))


# compare times from both methods
def alg_2(R=1):
    rho_i, rho_j = rng.pm(), rng.pm()
    r_i = R * sqrt(rho_i)
    phi_j = 2 * pi * rho_j
    return r_i, phi_j


timer1 = time()
for i in range(50000):
    alg_1()
timer1 = time() - timer1

timer2 = time()
for i in range(50000):
    alg_2()
timer2 = time() - timer2

print('Total time for alg_1 is:  {}'.format(timer1))
print('Total time for alg_2 is:  {}'.format(timer2))
