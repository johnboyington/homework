import numpy as np
import matplotlib.pyplot as plt
from interpolate import interpolate


x = np.linspace(1, 10, 20)
y = np.sin(x)


x_new = 5.1245


y_new = interpolate(x_new, x, y, len(y), 1)

plt.plot(x, y, 'ko')
# plt.plot(x_new, y_new, 'rx')
