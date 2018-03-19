import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

x, y = np.mgrid[-1:10:.01, -1:2:.01]
pos = np.empty(x.shape + (2,))
pos[:, :, 0] = x; pos[:, :, 1] = y
rv = multivariate_normal([0.5, -0.2], [[2.0, 0.3], [0.3, 0.5]])
rv = mv([5, 1], [[1, 0.05], [0.05, 0.25]])
plt.contourf(x, y, rv.pdf(pos))