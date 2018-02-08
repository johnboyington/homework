import numpy as np
import matplotlib.pyplot as plt

def plot(textfile, n):
    f = open(textfile, 'r')
    data = f.readlines()
    
    erg = []
    val = []
    
    for d in data:
        d = d.split()
        d = d[:-n]
        for i, v in enumerate(d):
            if i % 2 == 0:
                ve = float(v[:8] + 'E' + v[-2:]) * 1E-6
                erg.append(ve)
            else:
                ve = float(v[:8] + 'E' + v[-2:])
                val.append(ve)
    plt.figure(n)
    plt.plot(erg, val)
    plt.xlim(8E-12, 3)
    plt.ylim(4E-1, 2.5E3)
    plt.xscale('log')
    plt.yscale('log')

plot('resonance.txt', 3)
plot('elastic.txt', 4)