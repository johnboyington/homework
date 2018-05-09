import numpy as np
import matplotlib as pyplot
from sandii import iterate
from scipy.stats import norm
from scipy.optimize import curve_fit
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
sig = np.matrix(sig)
C_y = (1 / (len(sig.T) - 1)) * (sig.T * sig)
C_x = np.linalg.pinv(R) * C_y * np.linalg.pinv(R.T)
sandwich_error = np.sqrt(C_x.diagonal() * (len(f_i) - 1))

###############################################################################
#                           individual bin comparison
###############################################################################

analytical_error = np.zeros(len(f_i))

for g in range(len(f_i)):
    group = g
    group_mean = y_sum[group]
    group_data = y[:, group] * n
    
    hist_data = np.histogram(group_data, bins=25)
    hist = Spectrum(hist_data[1], hist_data[0])
    
    
    def gauss(x, mu, sig, A):
        return A * ((1 / np.sqrt(2 * np.pi * sig**2)) * np.exp(-(x - mu)**2 / (2 * sig**2)))
    
    c = curve_fit(gauss, hist.midpoints, hist.values, p0=[group_mean, group_mean, 100])[0]
    analytical_error[g] = abs(c[1])
    
    if g == 15:
        x_gauss = np.linspace(hist.stepu_x[0], hist.stepu_x[-1], 100)
        y_gauss = gauss(x_gauss, c[0], c[1], c[2] / n)
        
        fig = plt.figure(4)
        ax = fig.add_subplot(111)
        ax.plot(hist.stepu_x, hist.stepu_y / n, 'k', markersize=0.1, label='Histogram Data')
        ax.plot(x_gauss, y_gauss, 'indigo', label='Gaussean Fit')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.set_xlabel('Mean Value')
        ax.set_ylabel('Frequency')
        plt.savefig('bin_hist.png', dpi=300)





###############################################################################
#                           aux plots
###############################################################################
'''
fig = plt.figure(2)
ax = fig.add_subplot(111)
plt.plot(y[:, group] * n, 'ko', markersize=0.3)
plt.plot([0, n - 1], [y_sum[group], y_sum[group]], color='indigo')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

fig = plt.figure(3)
ax = fig.add_subplot(111)
ax.plot([1] * n, y[:, group] * n, 'ko', markersize=0.1)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
'''

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

###############################################################################
#                            L_2 norms tabulation
###############################################################################

L2_norm_error = np.sqrt(np.sum(error**2))
L2_norm_analytical_error = np.sqrt(np.sum(analytical_error**2))
sandwich_error = np.array(sandwich_error[0])
L2_norm_sandwich_error = np.sqrt(np.sum(sandwich_error**2))


###############################################################################
#                            comparerror
###############################################################################
error_spec = Spectrum(nebp.edges, error)
anal_spec = Spectrum(nebp.edges, analytical_error)
sand_spec = Spectrum(nebp.edges, sandwich_error[0])

fig = plt.figure(5)
ax = fig.add_subplot(111)
ax.plot(error_spec.step_x, error_spec.step_y, color='k', linestyle='-', label='Population Std. Dev.', linewidth=0.7,)
ax.plot(anal_spec.step_x, anal_spec.step_y, color='indigo', linestyle='--', label='Analytical Std. Dev.', linewidth=0.7,)
ax.plot(sand_spec.step_x, sand_spec.step_y, color='green', linestyle=':', label='Sandwich Std. Dev.', linewidth=0.7,)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('Energy $MeV$')
ax.set_ylabel('Error $cm^{-2}s^{-1}MeV^{-1}$')
ax.set_xlim(1E-9, 20)
plt.legend()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(frameon=False)
plt.savefig('error.png', dpi=300)

###############################################################################
#                            latex tabulation
###############################################################################


def latex_tabulate(sand, pop_error, analy):
    s = '''\\begin{{table*}}[h]
\\centering
\\begin{{tabular}}{{ |c|c|c|c| }}
 \\hline
 Energy Group & Sandwich Method Error & Population Std. Dev. & Analytical Std. Dev. \\\\
 \\hline
{}
 \\hline
\\end{{tabular}}
\\end{{table*}}'''

    rows = ''
    for i in range(len(sand)-1, 0, -1):
        rows += '     {} & {:9.6f} & {:8.6f} & {:8.6f}  \\\\ \n'.format(len(sand) - i, float(sand[i]), pop_error[i], analy[i])
    return s.format(rows)
    
table = latex_tabulate(sandwich_error.T, error, analytical_error)

with open('table.txt', 'w+') as F:
    F.write(table)














