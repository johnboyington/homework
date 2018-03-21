
fast_n = 5.28476E-03
tot_n = 5.72072E-03


gamma__n = 4.65816E-03
gamma_sep = 1.97087E-04
gamma_tot = gamma__n + gamma_sep

ft = fast_n / tot_n
ng = tot_n / gamma_tot

flux_in = 3 * 2.949E+08
flux_out = flux_in * tot_n


print('The FT ratio: {}'.format(ft))
print('The NG ratio: {}'.format(ng))
print('Incoming Flux: flux: {:10.6E} 1/cm^2s'.format(flux_in))
print('Outgoing Flux: {:10.6E} 1/cm^2s'.format(flux_out))
