'''
Fundamentals of Nuclear Reactor Physics
Chapter 5
Problem 5.15
'''
import numpy as np
import matplotlib.pyplot as plt

#define variables

beta = 0.007
gam = 5E-5 #s
lam = 0.08 #s-1
rho_a = 0.00175
rho_b = -rho_a
omega_new = 0.0001
rho = rho_a
omega = 1
n = 0

#while abs(omega - omega_new) > 0.01:
#    omega = omega_new
#    A = (rho - beta) / gam
#    B = (lam * beta) / (gam * (omega + lam))
#    omega_new = A + B
#    n += 1
#    print(n)
#    print(omega)
#    print(omega_new)
#
#print(omega)
#print(omega_new)
#print('T = {} s'.format(1 / omega))

omega = np.linspace(-1000, 1000, 4000)

A = (rho - beta) / gam
B = (lam * beta) / (gam * (omega + lam))
omega_new = A + B
print(omega_new)

plt.figure(0)
plt.xlim(-10, 10)
plt.ylim(-200, 10)
plt.plot(omega, omega_new - omega)