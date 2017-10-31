import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from matplotlib import rcParams
rcParams['xtick.direction'] = 'in'
rcParams['ytick.direction'] = 'in'

plt.ioff()
exp = np.exp 

def Q(rho_e, rho_h) :
    return rho_e + rho_e**2*(exp(-1.0/rho_e)-1.0) + \
           rho_h + rho_h**2*(exp(-1.0/rho_h)-1.0)
    
def sig_Q(rho_e, rho_h) :
    a = rho_e**2 + 2.*rho_e**3*(exp(-1.0/rho_e)-1) + \
        0.5*rho_e**3*(1-exp(-2.0/rho_e))
    b = rho_h**2 + 2.*rho_h**3*(exp(-1.0/rho_h)-1) + \
        0.5*rho_h**3*(1-exp(-2.0/rho_h))
    c = 2.*rho_e*rho_h + 2.*rho_e**2*rho_h*(exp(-1.0/rho_e)-1) + \
        2.*rho_h**2*rho_e*(exp(-1.0/rho_h)-1)
    d = 2.*(rho_e*rho_h)**2/(rho_e-rho_h)*(exp(-1.0/rho_e)-exp(-1.0/rho_h))
    return np.sqrt( a+b+c+d-Q(rho_e,rho_h)**2)
   
def R(rho_e, rho_h) :
    return 100*sig_Q(rho_e, rho_h)/Q(rho_e, rho_h)

def RR(per, rho_e):
    return per - R(rho_e, 100)
    
    
n = 1000
H = np.logspace(-2, 2, n)
E = np.logspace(-2, 2, n)

H, E = np.meshgrid(H, E, sparse=False, indexing='ij')
res = R(E, H)


# my code starts here
# set the contour line locations
peaks = np.array([0.1, 0.2, 0.5, 1, 2, 5, 10, 15, 20, 30, 40])

# create the figure and subplot objects and produce contour plot
fig = plt.figure(1, figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1)
ax.contour(E, H, res, colors='k', levels=peaks)

plt.xlabel('Electron Extraction Factor')
plt.ylabel('Hole Extraction Factor')

plt.xscale('log')
plt.yscale('log')

ticker = (0.1, 1, 10, 100)
plt.xticks(ticker, ticker)
plt.yticks(ticker, ticker)

plt.xlim(0.1, 100)
plt.ylim(0.1, 100)

# locations of the percentages
text = [(110, 73, '0.1%'),
        (110, 44, '0.2%'),
        (110, 23, '0.5%'),
        (110, 12.5, '1%'),
        (110, 6.5, '2%'),
        (110, 2.65, '5%'),
        (110, 1.27, '10%'),
        (110, .77, '15%'),
        (110, .55, '20%'),
        (110, .29, '30%'),
        (110, .16, '40%'),
        (.75, 110, '15%'),
        (.5, 110, '20%'),
        (.28, 110, '30%'),
        (.15, 110, '40%')]

for x, y, t in text:
    plt.text(x, y, t)



#for p in peaks:
#    print(RR(p))
#    z = sp.optimize.newton(RR, 10, args=(p))
#    plt.text(110, z, str(p))

plt.savefig('new_contour.png')
