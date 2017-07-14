#ne737 final project energy calibration
#calibration done using cs137 source

import matplotlib.pyplot as plt
import numpy as np

ch = range(1024)

d1 = list(np.loadtxt('calibration/calD1.Spe'))
d2 = list(np.loadtxt('calibration/calD2.Spe'))
d3 = list(np.loadtxt('calibration/calD3.Spe'))

plt.figure(0)
plt.title('Spectra Used for Calibration')
plt.xlabel('Channel')
plt.ylabel('Counts')
plt.plot(ch, d1, label='D1')
plt.plot(ch, d2, label='D2')
plt.plot(ch, d3, label='D3')
plt.legend()

p1 = d1[600:].index(max(d1[600:])) + 600
p2 = d2[600:].index(max(d2[600:])) + 600
p3 = d3[600:].index(max(d3[600:])) + 600

pks = np.array([p1, p2, p3])
erg = 662.
print erg / pks