# ne737 final project

import matplotlib.pyplot as plt
import numpy as np

def ZETA(SS, RR, oSS, oRR):
    top = (SS - RR)**2
    bot = oSS**2 + oRR**2
    return top / bot

def ROLL(Df, De, oDf, oDe):
    v = 9.0
    W = [-1, 0, 1]    
    T = []
    for i in [1, 2, 3]:
        for j in [1, 2]:
            S = 0
            for a in W:
                for b in W:
                    Z =  ZETA(Df[i+a, j+b], De[i+a, j+b], oDf[i+a, j+b], oDe[i+a, j+b])
                    S += Z
            T.append(S)
    return (np.array(T) / v).reshape(3,2)

def ROLL2(Df, De, oDf, oDe):
    v = 4.0
    W = [-1, 0]
    T = []
    for i in [1, 2, 3 , 4]:
        for j in [1, 2, 3]:
            S = 0
            for a in W:
                for b in W:
                    Z =  ZETA(Df[i+a, j+b], De[i+a, j+b], oDf[i+a, j+b], oDe[i+a, j+b])
                    S += Z
            T.append(S)
    return (np.array(T) / v).reshape(4,3)


D1f = np.loadtxt('data/sums/fd1.txt')
D2f = np.loadtxt('data/sums/fd2.txt')
D3f = np.loadtxt('data/sums/fd3.txt')
D1e = np.loadtxt('data/sums/ed1.txt') * 2
D2e = np.loadtxt('data/sums/ed2.txt') * 2
D3e = np.loadtxt('data/sums/ed3.txt') * 2

oD1f = np.sqrt(D1f)
oD2f = np.sqrt(D2f)
oD3f = np.sqrt(D3f)
oD1e = np.sqrt(D1e)
oD2e = np.sqrt(D2e)
oD3e = np.sqrt(D3e)



B1 = ROLL(D1f, D1e, oD1f, oD1e)
B2 = ROLL(D2f, D2e, oD2f, oD2e)
B3 = ROLL(D3f, D3e, oD3f, oD3e)

T1 = ROLL2(D1f, D1e, oD1f, oD1e)
T2 = ROLL2(D2f, D2e, oD2f, oD2e)
T3 = ROLL2(D3f, D3e, oD3f, oD3e)

S1 = D1e - D1f
S2 = D2e - D2f
S3 = D3e - D3f


n = [B1, B2, B3]
for ii in [1, 2, 3]:
    plt.figure(ii)
    plt.title('3x3 Rolling Window $\chi ^2$ Test for Detector {}'.format(ii))
    plt.imshow(n[ii - 1], cmap='Greys', vmin=0, vmax=np.max(n[ii - 1]))
    plt.savefig('plots/B{}.png'.format(ii))


n = [T1, T2, T3]
for ii in [1, 2, 3]:
    plt.figure(ii + 3)
    plt.title('2x2 Rolling Window $\chi ^2$ Test for Detector {}'.format(ii))
    plt.imshow(n[ii - 1], cmap='Greys', vmin=0, vmax=np.max(n[ii - 1]))
    plt.savefig('plots/T{}.png'.format(ii))

n = [S1, S2, S3]
for ii in [1, 2, 3]:
    plt.figure(ii + 6)
    plt.title('Direct Subtraction for Detector {}'.format(ii))
    plt.imshow(n[ii - 1], cmap='Greys', vmin=np.min(n[ii - 1]), vmax=np.max(n[ii - 1]))
    plt.savefig('plots/S{}.png'.format(ii))
    print n[ii -1]

