import numpy as np
import os
from casmo_temp import Casmo_Input, Casmo_Output


# for fuel
nt = 20
ftemps = np.linspace(700, 1200, nt)
# p_values = np.linspace(.3, .5, 10)
p_values = np.array([.39, .4, .41])

# for moderator
ctemps = np.linspace(300, 600, nt)


if __name__ == '__main__':
    def cycle(name, ID, tfu, tco, p):
        Casmo_Input(name, ID, tfu, tco, p)
        os.system('casmo4 {}.inp'.format(name))
        out = Casmo_Output('{}.out'.format(name), ID)
        os.system('rm *.inp')
        os.system('rm *.log')
        os.system('rm *.out')
        os.system('rm *.cax')
        return out.k_inf
    
    
    
    counter = 0
    data = []
    for t in ftemps:
        for p_val in p_values:
            k = cycle('temp{}'.format(counter), counter, t, 300, p_val)
            data.append((t, p_val, k))
            counter += 1
    
    with open('fuel.txt', 'w+') as F:
        for d in data:
            F.write('{} {} {}\n'.format(*d))
    
    
    
    
    counter = 0
    data = []
    for t in ctemps:
        for p_val in p_values:
            k = cycle('temp{}'.format(counter), counter, 900, t, p_val)
            data.append((t, p_val, k))
            counter += 1
    
    with open('coolant.txt', 'w+') as F:
        for d in data:
            F.write('{} {} {}\n'.format(*d))
