from parameters import Parameters
from material import material_library, rand_material
from numpy.random import randint
import os
import subprocess
import re
from fitness_function import fitness


class Core(object):

    def __init__(self, ID, chromosome):
        self.ID = ID
        assert type(chromosome) is list, 'chromosome must be of type list'
        self.params = Parameters()
        self.chromosome = chromosome
        self.decode_materials()
        self.fitness = -1

    def decode_materials(self):
        self.materials = []
        for i in self.chromosome:
            self.materials.append(material_library[i])

    def write(self):
        '''
        Writes the input file for this particular core.
        '''
        default_text = open('bwr_bundle.temp', 'r').read().split('*FLAG*')
        s = default_text[0]
        for i, m in enumerate(self.materials):
            u, g = m
            if g == 0:
                s += 'FUE  {:2d}  10.5 / {:5.1f}\n'.format(i+1, u)
            else:
                s += 'FUE  {:2d}  10.2 / {:5.1f} 64016 = {:5.1f}\n'.format(i+1, u, g)
        s += 'LFU\n'

        # do something crazy
        tri = ''
        n = 1
        j = 0
        for i in range(1, len(self.materials) + 1):
            if i == 19 or i == 20 or i == 25 or i == 26:
                tri += '  0'
                j += 1
            else:
                tri += '{:3d}'.format(i)
                j += 1
            if j == n and n != 10:
                tri += '\n'
                j = 0
                n += 1
        s += tri
        s += default_text[1]
        with open('core{}.inp'.format(self.ID), 'w+') as F:
            F.write(s)

    def extract(self):
        # extract data
        with open('core{}.out'.format(self.ID), 'r') as f:
            output = f.read().split('** C A S M O - 4E SUMMARY **')[1].split('DAYS')[1].split('RUN')[0].split('\n')[1:-3]
        burnup = []
        pppf = []
        k_inf = []
        for line in output:
            line = line.split()
            burnup.append(float(line[-10]))
            pppf.append(float(line[-6]))
            k_inf.append(float(line[-9]))

        # calculate fitness
        self.eol_burnup = burnup[-1]
        self.max_pppf = max(pppf)
        self.max_k_inf = max(k_inf)
        self.fitness = fitness(self.eol_burnup, self.max_pppf, self.max_k_inf)

        # consider fitness constraints
        if k_inf[0] < 1:
            self.fitness = 0
        for k in k_inf:
            if k > 1.13:
                self.fitness = 0
        for p in pppf:
            if p > 1.35:
                self.fitness = 0

        # remove file
        subprocess.call(['rm core{}*'.format(self.ID)], shell=True)

    def run_local(self):
        self.write()
        with open('dump{}.txt'.format(self.ID), 'w+') as dump:
            subprocess.call(['/share/apps/studsvik/bin/casmo4', 'core{}.inp'.format(self.ID)], stdout=dump)
        subprocess.call(['rm', 'dump{}.txt'.format(self.ID)])
        self.extract()

    def get_fitness(self):
        return self.fitness


if __name__ == '__main__':
    c = []
    for i in range(55):
        c += [randint(0, len(material_library))]
    indiv = Core(0, c)
    indiv.run_local()
    print('\n\n')
    print('------------------')
    print(indiv.fitness)
    print('------------------')
