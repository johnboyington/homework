import numpy as np
from numpy.random import rand

B = np.array([[0.4, 0.10, 0.10, 0.20],
              [0.10, -0.50, 0.10, 0.20],
              [0.10, 0.20, -0.40, 0.10],
              [0.10, 0.20, 0.10, 0.10]])

P = np.array([[0.60, 0.10, 0.10, 0.10],
              [0.10, 0.60, 0.10, 0.10],
              [0.05, 0.10, 0.60, 0.05],
              [0.20, 0.20, 0.20, 0.20]])

p = np.array([0.25, 0.25, 0.25, 0.25])
f = np.array([-0.7, 1.8, 3.3, 2.8])
h = np.array([1, 1, 1, 1])

# Samples from a given probability vector
# Note that cumsum is the cummulative sum vector


def sample(rho, P):
    j = 0
    found = False
    while not found:
        if rho <= np.cumsum(P)[j]:
            found = True
        else:
            j += 1
    return j

k = 100
Z = 0
samps = 10**6
for n in range(samps):
    # determine initial value i0
    i0 = sample(rand(), p)
    # Perform a random walk with 'k' steps or until terminated
    S = 0
    U = 1
    i = i0
    walk = 0
    while walk < k:
        rho = rand()
        # Determine if the walk is terminated by the kill vector
        if rho > np.cumsum(P[i])[-1]:
            walk = k
        # Perform the walk, update 'U' and advance the step
        else:
            j = sample(rho, P[i])
            U = U * (B[i, j] / P[i, j])
            i = j
            walk += 1
    # sum Z estimates calculaated for absorption states
    Z += (h[i0]/p[i0])*U*(f[i]/(1-np.cumsum(P[i])[-1]))
print(Z/samps)
