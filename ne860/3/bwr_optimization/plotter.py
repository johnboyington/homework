from parameters import Parameters
import matplotlib.pyplot as plt
import numpy as np


class Plot(object):

    def __init__(self):
        self.params = Parameters()
        self.get_data()
        self.plot_legacy()
        self.plot_ratios()

    def get_data(self):
        self.data = np.loadtxt('data.txt').reshape(self.params.num_gens + 1, self.params.start_size, -1)

    def plot_legacy(self):
        plt.figure(30)
        for n, i in enumerate(self.data):
            i = i.T
            plt.plot(range(self.params.start_size), i[0], label='gen {}'.format(n))
        plt.xlabel('Individual (Ordered by Fitness)')
        plt.ylabel('Fitness')
        plt.legend()
        plt.savefig('legacy.png', dpi=250)

    def plot_ratios(self):
        plt.figure(31)
        for i, n in enumerate(self.data):
            ft = []
            ng = []
            for nn in n:
                ft.append(nn[1])
                ng.append(nn[2])
            plt.plot(ft, ng, linestyle='none', marker='o', markersize=2, label='gen {}'.format(i))
        plt.xlabel('Fast to Total Ratio')
        plt.ylabel('Neutron to Gamma Ratio')
        plt.xlim(0.85, 1)
        plt.ylim(0, 10)
        #plt.legend()
        plt.savefig('ratios.png', dpi=250)


if __name__ == '__main__':
    plot = Plot()
