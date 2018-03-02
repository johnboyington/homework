'''
Process Mike's Output Files

'''
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams
from casmo import Casmo_Output

# nice plots
rc('font', **{'family': 'serif'})
rcParams['xtick.direction'] = 'out'
rcParams['ytick.direction'] = 'out'
rcParams['xtick.labelsize'] = 12
rcParams['ytick.labelsize'] = 12
rcParams['lines.linewidth'] = 1.85
rcParams['axes.labelsize'] = 15
rcParams.update({'figure.autolayout': True})


output = []
files = os.listdir('files')
for f in files:
    if '.out' in f:
        num = int(f[6:-8])
        out = Casmo_Output('files/' + f, num)
        output.append(out)


def key(o):
    return o.ID
output = sorted(output, key=key)

nums = []
etas = []
ps = []
epsilons = []
k_infs = []

for i in output:
    nums.append(i.ID)
    etas.append(i.eta)
    ps.append(i.p)
    epsilons.append(i.epsilon)
    k_infs.append(i.k_inf)

p_d = np.linspace(0.01, 0.7, 100) * 2
p_d = p_d[:len(nums)]
p_d = 1.2598 / p_d
fig = plt.figure(0)
ax = fig.add_subplot(111)
ax.set_xlabel('$P/D$')
ax.plot(p_d, etas, label='$\eta$')
ax.plot(p_d, ps, label='$p$')
ax.plot(p_d, epsilons, label='$\epsilon$')
ax.plot(p_d, k_infs, label='$k_{inf}$')
ax.legend()
plt.savefig('geometry.png', dpi=300)
