import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

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

def RR(rho_e):
    return 100 - R(rho_e, 100)
    
    
n = 100
H = np.logspace(-2, 2, n)
E = np.logspace(-2, 2, n)

H, E = np.meshgrid(H, E, sparse=False, indexing='ij')
res = R(E, H)


# my code starts here
peaks = np.array([0.1, 0.2, 0.5, 1, 2, 5, 10, 15, 20, 30, 40])

plt.figure(1, figsize=(8, 8))
plt.contour(np.log10(E), np.log10(H), res, colors='k', levels=peaks)


plt.xlabel('Electron Extraction Factor')
plt.ylabel('Hole Extraction Factor')


plt.xticks((-1, 0, 1, 2), (0.1, 1, 10, 100))
plt.xlim(-1, 2)

plt.yticks((-1, 0, 1, 2), (0.1, 1, 10, 100))
plt.ylim(-1, 2)


for p in peaks:
    print(RR(p))
    z = sp.optimize.newton(RR, 10)
    plt.text(110, np.log10(z), str(p))


#ticks = H
#plt.gca().yaxis.set_ticks(np.log10(ticks))



plt.savefig('new_contour.png')
