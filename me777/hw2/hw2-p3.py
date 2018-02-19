'''
me777 hw2 problem 2
'''
from numpy import sin, full, sqrt
from numpy.random import rand
import matplotlib.pyplot as plt


def integrate(n):
    y1true = 2.0000
    y2true = 1.1869
    y1 = 0
    y2 = 0
    n = int(n)
    for i in range(n):
        x = rand()
        y1 += (1 / (rand()**0.5))
        y2 += sin(x) / (sqrt(1 - x))
    y1 = y1 / n
    y2 = y2 / n
    err1 = abs(y1true - y1) / y1true
    err2 = abs(y2true - y2) / y2true
    return y1, err1, y2, err2

vals1 = []
vals2 = []
errs1 = []
errs2 = []


enns = [1E1, 1E2, 1E3, 1E4, 1E5, 1E6]
for i in enns:
    data = integrate(i)
    vals1.append(data[0])
    errs1.append(data[1])
    vals2.append(data[2])
    errs2.append(data[3])

# plotting
fig = plt.figure(0, figsize=(9.62, 5.08))
ax = fig.add_subplot(111)
ax.plot(enns, vals1, label='MC Result', color='darkblue', linestyle='--')
ax.plot(enns, full(len(enns), 2.0000), label='Integral 1', color='grey')
ax.set_xlabel('N')
ax.set_ylabel('Value')
ax.set_xscale('log')
ax.legend()
fig.savefig('integral1.png', dpi=300)

# plotting
fig = plt.figure(1, figsize=(9.62, 5.08))
ax = fig.add_subplot(111)
ax.plot(enns, vals2, label='MC Result', color='indigo', linestyle='--')
ax.plot(enns, full(len(enns), 1.1869), label='Integral 2', color='grey')
ax.set_xlabel('N')
ax.set_ylabel('Value')
ax.set_xscale('log')
ax.legend()
fig.savefig('integral2.png', dpi=300)


# plotting
fig = plt.figure(2, figsize=(9.62, 5.08))
ax = fig.add_subplot(111)
ax.plot(enns, errs1, label='Error 1', color='red', linestyle='--')
ax.plot(enns, errs2, label='Error 2', color='green')
ax.set_xlabel('N')
ax.set_ylabel('Percent Error')
ax.set_xscale('log')
ax.set_yscale('log')
ax.legend()
fig.savefig('error.png', dpi=300)
