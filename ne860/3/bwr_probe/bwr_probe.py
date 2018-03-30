from core import Core
from material import material_library, rand_material, mat_id
from numpy.random import randint
import numpy as np
import matplotlib.pyplot as plt


class Probe(object):
    def __init__(self):
        self.individuals(False)
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
        [(2,4),
         (2.2,0), (2.5,0), 
         (2.5,0), (3.0,0), (3.5,0), 
         (3.0,2), (3.0,0), (3.7,0), (3.0,0), 
         (3.0,2), (3.0,0), (3.7,0), (3.0,0), (3.0,0), 
         (3.0,2), (3.0,0), (3.0,0), (2.0,2), (2.0,2), (3.0,0), 
         (2.5,0), (3.0,0), (3.0,0), (2.0,2), (2.0,2), (3.0,0), (4.0,0), 
         (2.5,0), (3.0,0), (3.0,0), (3.0,0), (3.0,0), (3.4,0), (4.2,0), (4.0,0), 
         (2.0,0), (3.0,0), (3.0,0), (3.0,0), (3.0,0), (3.0,0), (3.0,0), (3.0,0), (3.0,0), 
         (2.0,0), (2.0,0), (2.5,2), (2.5,2), (2.5,2), (2.5,2), (3.0,0), (2.5,0), (2.0,0), (2,4)]
        
        c = []
        for f in fuel:
            c.append(mat_id(*f))
        indiv = Core(206, c)
        indiv.write()
        if ran:
            indiv.extract()
            self.plot_individual(indiv)

    def plot_individual(self, ind):
        print('\n\n')
        print('------------------')
        print('Individual:  {}'.format(ind.ID))
        print(ind.fitness)
        print('------------------')
        # plot core map
        fig = plt.figure(1, figsize=(10, 8))
        ax = fig.add_subplot(224)
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


Probe()
