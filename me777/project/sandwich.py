import numpy as np
import matplotlib as pyplot
from sandii import iterate
from scipy.stats import norm
from numpy.random import rand
import matplotlib.pyplot as plt
from time import time
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

n = 2500
y = np.zeros((n, len(f_i)))
y2 = np.zeros((n, len(f_i)))

'''
fig = plt.figure(2)
ax = fig.add_subplot(111)
'''
ran = True
t_i = time()
if not ran:
    for i in range(n):
        sol = iterate(f_i, sample(N, sig), sig, R)
        sol_spec = Spectrum(nebp.edges, sol)
        y[i] = (sol)/n
        y2[i] = (sol**2)/n
        # ax.plot(sol_spec.step_x, sol_spec.step_y)

    np.save('y.npy', y)
    np.save('y2.npy', y2)

t_f = time() - t_i
print('\ntime:  {}\n'.format(t_f))
y = np.load('y.npy')
y2 = np.load('y2.npy')

y_sum = np.sum(y, axis=0)
y2_sum = np.sum(y2, axis=0)


'''
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('Energy $MeV$')
ax.set_ylabel('Flux $cm^{-2}s^{-1}MeV^{-1}$')
ax.set_xlim(1E-9, 20)
plt.legend()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(frameon=False)
'''


###############################################################################
#                                sandwich comparison
###############################################################################
N = np.matrix(N)
C_y = (1 / (len(N.T) - 1)) * (N.T * N)
C_x = np.linalg.pinv(R) * C_y * np.linalg.pinv(R.T)
sandwich_error = np.sqrt(C_x.diagonal() * (len(f_i) - 1))

###############################################################################
#                           individual bin comparison
###############################################################################

group = 20
plt.plot(y[:, group] * n, 'ko', markersize=0.3)
plt.plot([0, n - 1], [y_sum[group], y_sum[group]], color='indigo')


###############################################################################
#                                final comparison
###############################################################################

error = np.sqrt((n / (n - 1)) * (y2_sum - y_sum**2))
solution = Spectrum(nebp.edges, y_sum, error)
# error = sandwich_error

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
