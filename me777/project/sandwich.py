import numpy as np
import matplotlib as pyplot
from sandii import iterate
from scipy.stats import norm
from numpy.random import rand
import matplotlib.pyplot as plt

# sandwich method

R = np.array([[1, 2, 3, 2], [3, 2, 1, 1]], dtype=np.float64)
f_i = np.array([1, 1, 1, 1], dtype=np.float64)
N = np.array([2, 2.5], dtype=np.float64)
sig = np.array([0.1, 0.1], dtype=np.float64)

sol = iterate(f_i, N, sig, R)

def sample(responses, errors):
    l = len(responses)
    sampled_response = np.zeros(l)
    for i in range(l):
        resp = responses[i]
        err = errors[i]
        fun = norm(loc=resp, scale=err)
        rho = rand()
        sampled_response[i] = fun.ppf(rho)
    return sampled_response

y = np.zeros(len(f_i))
y2 = np.zeros(len(f_i))

n = 10
for i in range(n):
    sol = iterate(f_i, sample(N, sig), sig, R)
    y += (sol)/n
    y2 += (sol**2)/n

error = (1 / (n - 1)) * (y**2 - y2)
plt.plot(y)
plt.errorbar(range(4), y, error)
    