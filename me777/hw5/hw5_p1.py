import numpy as np
from numpy import pi, sin
from numpy.random import rand

R_sol = 0.814183

def Integral(sig):
    I = 0
    n = 100000
    for i in range(n):
        x = rand() * (pi/2)
        I += sin(x)**sig
    return (I / n) * (pi/2)



L, R = 0, 2
found = False
bounds = 0.0001

while not found:
    print(L, R)
    points = np.linspace(L, R, 4)
    
    integrals = np.zeros(len(points))
    for i, p in enumerate(points):
        integrals[i] = Integral(p)
    
    for j in range(len(integrals) - 1):
        Hi, Lo = max(integrals[j], integrals[j+1]), min(integrals[j], integrals[j+1])
        if R_sol > Lo and R_sol < Hi:
            L, R = points[j], points[j+1]
            solution = points[j], integrals[j]
            if abs(solution[1] - R_sol) < bounds:
                found = True
                break

print('Sigma =  ', solution)
sol_I = Integral(solution[0])
print('Sol_I =  ', sol_I)
