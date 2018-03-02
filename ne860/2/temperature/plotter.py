import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams
import casmo_manager as cm

fuel_data = np.loadtxt('fuel.txt')
fuel_data = fuel_data.reshape(len(cm.ftemps), len(cm.p_values), -1)

coolant_data = np.loadtxt('coolant.txt')
coolant_data = coolant_data.reshape(len(cm.ctemps), len(cm.p_values), -1)


rc('font', **{'family': 'serif'})
rcParams['xtick.direction'] = 'out'
rcParams['ytick.direction'] = 'out'
rcParams['xtick.labelsize'] = 12
rcParams['ytick.labelsize'] = 12
rcParams['lines.linewidth'] = 1.85
rcParams['axes.labelsize'] = 15
rcParams.update({'figure.autolayout': True})


def plot(data, n, temps, name):
    a_f = np.zeros((len(temps)-1, len(cm.p_values)))
    for t in range(0, len(temps)-1):
        for p in range(0, len(cm.p_values)):
            A = (1 / data[t, p, 2])
            B = (data[t+1, p, 2] - data[t, p, 2])
            C = (data[t+1, p, 0] - data[t, p, 0])
            a_f[t, p] = A * (B / C)

    p_d = cm.p_values * 2
    p_d = 1.2598 / p_d

    a_f = a_f.T
    fig = plt.figure(n)
    ax = fig.add_subplot(111)
    for i, t in enumerate(a_f):
        ax.plot(temps[:-1], t)
    ax.legend(p_d)
    ax.set_xlabel('Temperature $K$')
    ax.set_ylabel(r'$\alpha_{T_F}$')
    fig.savefig(name + '.png', dpi=300)

plot(fuel_data, 0, cm.ftemps, 'fuel')
plot(coolant_data, 1, cm.ctemps, 'coolant')
