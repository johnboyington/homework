from core import Core
from material import material_library, rand_material, mat_id
from numpy.random import randint
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams

# nice plots
rc('font', **{'family': 'serif'})
rcParams['xtick.direction'] = 'out'
rcParams['ytick.direction'] = 'out'
rcParams['xtick.labelsize'] = 12
rcParams['ytick.labelsize'] = 12
rcParams['lines.linewidth'] = 1.85
rcParams['axes.labelsize'] = 15
rcParams.update({'figure.autolayout': True})


class Probe(object):
    def __init__(self):
        self.individuals(True)
        # self.test()

    def test(self):
        c = []
        for i in range(55):
            c += [randint(0, len(material_library))]
        indiv = Core(0, c)
        indiv.run_local()
        print('\n\n')
        print('------------------')
        print(indiv.fitness)
        print('------------------')
        self.plot_individual(indiv)

    def grid_probe(self):
        mesh = np.zeros((4, 4))
        for i, n in enumerate([3, 3.5, 4, 4.5]):
            for j, g in enumerate([0, 2, 3, 5]):
                num = mat_id(n, g)
                c = []
                for z in range(55):
                    c += [num]
                core = Core(100+10*i+j, c)
                core.extract()
                mesh[i, j] = core.fitness
                # print(core.eol_burnup)

        # plot values
        fig = plt.figure(100)
        ax = fig.add_subplot(111)
        image = ax.imshow(mesh, cmap='inferno')
        fig.colorbar(image)

    def individuals(self, ran):
        fuel = \
        [(2.0,0),
         (2.2,0), (3.0,0), 
         (2.5,0), (3.8,0), (4.0,0), 
         (3.2,0), (4.0,0), (4.5,0), (4.0,0), 
         (3.2,0), (4.0,0), (4.0,0), (3.0,0), (3.5,0), 
         (3.2,0), (4.5,0), (4.0,0), (2.0,0), (2.0,0), (3.5,0), 
         (3.2,0), (4.5,0), (4.0,0), (2.0,0), (2.0,0), (3.5,0), (4.0,0), 
         (3.0,0), (3.5,0), (4.0,0), (4.0,0), (4.0,0), (4.2,0), (4.5,0), (4.0,0), 
         (2.0,10), (3.2,2), (4.0,0), (4.0,0), (4.0,0), (4.0,0), (4.0,0), (4.0,0), (3.5,0), 
         (2.0,10), (2.0,10), (3.0,0), (3.2,0), (3.2,0), (2.8,0), (3.0,0), (2.5,0), (2.0,0), (2.0,0)]
        
        c = []
        for f in fuel:
            c.append(mat_id(*f))
        indiv = Core(235, c)
        indiv.write()
        if ran:
            indiv.extract()
            self.plot_individual(indiv)
        
        gad = np.zeros((10,10))
        en = np.zeros((10,10))
        indices = np.tril_indices(55)
        for i, f in enumerate(fuel):
            gad[indices[0][i], indices[1][i]] = f[1]
            en[indices[0][i], indices[1][i]] = f[0]
            print(f[1])
        fig = plt.figure(10)
        ax = fig.add_subplot(111)
        image = ax.imshow(gad, cmap='YlOrBr')
        fig.colorbar(image)
        fig.savefig('gad.png', dpi=300)

        # enrichment
        fig = plt.figure(11)
        ax = fig.add_subplot(111)
        image = ax.imshow(en, cmap='Reds')
        fig.colorbar(image)
        fig.savefig('enrichment.png', dpi=300)
        

    def plot_individual(self, ind):
        print('\n\n')
        print('------------------')
        print('Individual:  {}'.format(ind.ID))
        print(ind.fitness)
        print('------------------')
        # plot core map
        fig = plt.figure(1, figsize=(10, 8))
        ax = fig.add_subplot(224)
        ax.set_xlabel('EOL pppf')
        extreme = max(abs(1-ind.coremap.min()), abs(1-ind.coremap.max()))
        image = ax.imshow(ind.coremap, cmap='bwr', vmin=1-extreme, vmax=1+extreme)
        fig.colorbar(image)

        # plot k_inf over time
        ax = fig.add_subplot(221)
        ax.set_xlabel('Burnup Step')
        ax.set_ylabel('$K_{inf}$')
        ax.plot([0, len(ind.k_inf)], [1.13, 1.13], 'k')
        ax.plot([0, len(ind.k_inf)], [1.00, 1.00], 'k')
        ax.plot([0, len(ind.k_inf)], [0.95, 0.95], 'k')
        ax.plot(ind.k_inf)

        # plot pppf over time
        ax = fig.add_subplot(222)
        ax.set_xlabel('Burnup Step')
        ax.set_ylabel('pppf')
        ax.plot([0, len(ind.k_inf)], [1.30, 1.30], 'k')
        ax.plot(ind.pppf)

        # plot burnup over time
        ax = fig.add_subplot(223)
        ax.set_xlabel('Burnup Step')
        ax.set_ylabel('Burnup')
        ax.plot(ind.burnup)

        # save
        fig.savefig('best.png', dpi=300)
        


Probe()

'''
232
'''
