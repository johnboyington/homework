'''
me777 hw2 problem 2
'''
import numpy as np
from numpy.random import randint
import matplotlib.pyplot as plt
from spectrum import Spectrum


loaded = [1, 2, 3, 4, 5, 6, 6]
fair = [1, 2, 3, 4, 5, 6]

loaded_count = np.zeros(12)
fair_count = np.zeros(12)

n = 1000000
for i in range(n):
    ind1, ind2 = randint(0, 7), randint(0, 7)
    score = loaded[ind1] + loaded[ind2]
    loaded_count[score - 1] += 1

for i in range(n):
    ind1, ind2 = randint(0, 6), randint(0, 6)
    score = fair[ind1] + fair[ind2]
    fair_count[score - 1] += 1

loaded_count = loaded_count / n
fair_count = fair_count / n

edges = np.array(range(13)) + 0.5
loaded_data = Spectrum(edges[1:], loaded_count[1:])
fair_data = Spectrum(edges[1:], fair_count[1:])


var = 0
for i, val in enumerate(loaded_count[1:]):
    var += (7 - (i+2))**2 * val

print('The variance is:  {}'.format(var))


# plotting
fig = plt.figure(999, figsize=(9.62, 5.08))
ax = fig.add_subplot(111)
ax.plot(loaded_data.step_x, loaded_data.step_y, label='Loaded Dice', color='darkblue')
ax.plot(fair_data.step_x, fair_data.step_y, label='Fair Dice', color='green', linestyle='--')
ax.set_xlabel('Value')
ax.set_ylabel('Probability')
ax.legend()
