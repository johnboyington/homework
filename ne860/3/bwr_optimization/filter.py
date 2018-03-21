from parameters import Parameters
from material import test_library
import os
import subprocess
import re
from fitness_function import fitness


class Filter(object):

    def __init__(self, ID, chromosome):
        self.ID = ID
        assert type(chromosome) is list, 'chromosome must be of type list'
        self.params = Parameters()
        self.chromosome = chromosome
        self.length = self.chromosome[0]
        self.materials = self.chromosome[1:]
        self.get_materials()
        self.fitness = -1

    def get_materials(self):
        self.material_bank = test_library.lib

    def write(self):
        default_text = open('neutron_template.i', 'r').read().split('*FLAG*')
        s = default_text[0]
        for d in range(self.params.num_disc):
            m = self.material_bank[self.materials[d]]
            args = [200 + d, m.num, -m.density, 130 + d, 131 + d, m.name]
            s += '{}  {} {:9.5f} 120 -121 122 -123  {} -{}   $ {}\n'.format(*args)
        s += default_text[1]
        s += '90 0 -32 #11 #12 #13 (-130:-120:121:-122:123:{}) #31\n'.format(130+self.params.num_disc)
        s += default_text[2]
        for d in range(self.params.num_disc):
            args = [131 + d, self.length * ((d + 1) / self.params.num_disc)]
            s += '{} PX  {:9.5f}\n'.format(*args)
        s += '41  PX  {:9.5f}     $ Detector\n'.format(self.length + 0.0002)
        s += default_text[3]
        s += 'IMP:n 1 {}r 0\n'.format(self.params.num_disc + 4)
        s += 'IMP:p 1 {}r 0\n'.format(self.params.num_disc + 4)
        s += default_text[4]
        for m in set(self.materials + [0, 1, 2, 3]):
            mat = self.material_bank[m]
            s += 'c  -----------------------------------------------------------------------------\n'
            s += 'c  MATERIAL  {:3d}: {}\n'.format(mat.num, mat.name)
            s += 'c  -------------------------------------(density {:8.5} g/cm^3)---------------\n'.format(mat.density)
            for i, comp in enumerate(mat.composition):
                if i == 0:
                    card = 'M{}'.format(mat.num)
                else:
                    card = '    '
                s += '{}      {}   {}\n'.format(card, comp[0], comp[1])
            s += 'c\n'
        s += default_text[5]
        with open('{}n.i'.format(self.ID), 'w+') as F:
            F.write(s)

    def extract_neutron(self):
        with open('{}n.io'.format(self.ID), 'r') as f:
            mcnpOutput = f.read()
        s = r'1tally'
        tallyLocator = re.compile(s)
        tallyIndx = tallyLocator.finditer(mcnpOutput)
        indx = []
        for match in tallyIndx:
            indx.append(match.span()[1])
        s = r'\d.\d\d\d\dE[+-]\d\d   \d.\d\d\d\d\dE[+-]\d\d \d.\d\d\d\d'
        dataPtrn = re.compile(s)
        keys = [11, 21]
        d = {keys[0]: {'energy': [], 'value': [], 'sigma': []}, keys[1]: {'energy': [], 'value': [], 'sigma': []}}
        for i in range(len(keys)):
            data = dataPtrn.finditer(mcnpOutput[indx[i]:indx[i + 1]])
            for datum in data:
                dataStr = datum.group().split()
                d[keys[i]]['energy'].append(float(dataStr[0]))
                d[keys[i]]['value'].append(float(dataStr[1]))
                d[keys[i]]['sigma'].append(float(dataStr[2]))
        self.n_tot = d[11]['value'][4] + d[11]['value'][5]
        self.n_g = d[21]['value'][4] + d[21]['value'][5]
        try:
            self.fast_to_total = d[11]['value'][5] / self.n_tot
        except:
            self.fast_to_total = -1

    def extract(self):
        self.extract_neutron()
        subprocess.call(['rm {}n.i*'.format(self.ID)], shell=True)
        self.extract_gamma()
        subprocess.call(['rm {}g.i*'.format(self.ID)], shell=True)
        try:
            self.neutron_to_gamma = self.n_tot / (self.g_g + self.n_g)
        except:
            self.neutron_to_gamma = -1

    def calc_fitness(self):
        if self.neutron_to_gamma == -1 or self.fast_to_total == -1:
            self.fitness = 0
        else:
            self.fitness = fitness(self.fast_to_total, self.neutron_to_gamma, self.n_tot)

    def get_fitness(self):
        return self.fitness

    def run_local(self):
        self.write()
        with open('dump{}.txt'.format(self.ID), 'w+') as dump:
            subprocess.call(['casmo4', 'name={}n.i'.format(self.ID)], stdout=dump)
        subprocess.call(['rm', 'dump{}.txt'.format(self.ID)])
        self.extract()
        self.calc_fitness()


if __name__ == '__main__':
    c = [10, 1, 2, 3, 2, 2, 1, 2, 1, 2, 3, 1, 2, 3, 1, 2, 2, 1, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1, 1, 2, 1]
    indiv = Filter(0, c)
    indiv.write()
    indiv.run_local()
    indiv.extract()
    indiv.calc_fitness()
    print('------------------')
    print(indiv.fitness)
    print('------------------')
