#Homework 1 Problem 3
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.integrate as integrate
import scipy.special as sp

from mpl_toolkits.mplot3d import Axes3D


def qflux(qq_ref, RR_e, HH_e):
    return lambda rr, zz : qq_ref * np.cos((np.pi * zz) / HH_e) * sp.jv(0, (2.405 * rr) / RR_e)
    
def qdensity(qq_ref, RR_e, HH_e):
    return lambda rr, zz : qq_ref * np.cos((np.pi * zz) / HH_e) * sp.jv(0, (2.405 * rr) / RR_e) * (1 / (2 * np.pi))

#input parameters
P = 3411.0E6 #Wth
D = 337. #cm
R = D / 2. #cm
H = 366. #cm
dH = 10. #cm
dR = 10. #cm
R_e = R + dR #cm
H_e = H + dH #cm
q_ref = 100 #W
r = np.arange(0, R, 0.1685)
z = np.arange(-H/2, H/2, 0.366)
R,Z = np.meshgrid(r, z)

q_pp = qflux(q_ref, R_e, H_e)
print np.max(q_pp(R,Z))
print np.average(q_pp(R,Z))

peakavg_flux = np.max(q_pp(R,Z)) / np.average(q_pp(R,Z))
print peakavg_flux

q_ppp = qdensity(q_ref, R_e, H_e)
peakavg_density = np.max(q_ppp(R,Z)) / np.average(q_ppp(R,Z))
print np.max(q_ppp(R,Z))
print np.average(q_ppp(R,Z))
print peakavg_density