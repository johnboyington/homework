from numpy.random import rand


def sphere():
    rho = rand()
    r = 3 * rho**(1./3)
    if r < 1:
        return True


def cube():
    rho1, rho2, rho3 = rand(), rand(), rand()
    r = (rho1**2 + rho2**2 + rho3**2)**(0.5)
    if r < 1:
        return True

n = 10000
s_count = 0
c_count = 0
for i in range(n):
    s = sphere()
    if s:
        s_count += 1
    c = cube()
    if c:
        c_count += 1

print('Efficiency of Sphere (M=3):  {}'.format(s_count/n))
print('Efficiency of Cube:  {}'.format(c_count/n))
