import numpy as np
import matplotlib as pyplot
from sandii import iterate
from scipy.stats import norm
from numpy.random import rand
import matplotlib.pyplot as plt

from matplotlib import rc, rcParams
from nebp_response_functions import response_matrix
from experimental_data import unfiltered1
from spectrum import Spectrum
from nebp_spectrum import FluxNEBP
from nebp_unfolded_data import unfolded_data


# nice plots
rc('font', **{'family': 'serif'})
rcParams['xtick.direction'] = 'out'
rcParams['ytick.direction'] = 'out'
rcParams['xtick.labelsize'] = 12
rcParams['ytick.labelsize'] = 12
rcParams['lines.linewidth'] = 1.85
rcParams['axes.labelsize'] = 15
rcParams.update({'figure.autolayout': True})

nebp = FluxNEBP(250)

R = response_matrix
f_i = nebp.values
N = unfiltered1.values
sig = unfiltered1.error

sol = iterate(f_i, N, sig, R)
solution = Spectrum(nebp.edges, sol)

from_gravel = unfolded_data['e1_ne_gr']


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


###############################################################################
#                                iterative comparison
##############################################################################

n = 10
fig = plt.figure(2)
ax = fig.add_subplot(111)

for i in range(n):
    sol = iterate(f_i, sample(N, sig), sig, R)
    sol_spec = Spectrum(nebp.edges, sol)
    y += (sol)/n
    y2 += (sol**2)/n
    ax.plot(sol_spec.step_x, sol_spec.step_y)

ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('Energy $MeV$')
ax.set_ylabel('Flux $cm^{-2}s^{-1}MeV^{-1}$')
ax.set_xlim(1E-9, 20)
plt.legend()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(frameon=False)


error = np.sqrt((n / (n - 1)) * (y2 - y**2))
solution = Spectrum(nebp.edges, y, error)


###############################################################################
#                                final comparison
###############################################################################
fig = plt.figure(0)
ax = fig.add_subplot(111)
ax.plot(nebp.step_x, nebp.step_y, color='k', label='Default Spectrum', linewidth=0.7,)
ax.plot(solution.step_x, solution.step_y, color='indigo', label='Unfolded Spectrum', linewidth=0.7,)
ax.errorbar(solution.midpoints, solution.normalized_values, solution.error / solution.widths, linestyle='None', color='indigo', linewidth=0.7,)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('Energy $MeV$')
ax.set_ylabel('Flux $cm^{-2}s^{-1}MeV^{-1}$')
ax.set_xlim(1E-9, 20)
plt.legend()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(frameon=False)
plt.savefig('comparison.png', dpi=300)
    