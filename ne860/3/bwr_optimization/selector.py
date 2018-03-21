import numpy as np
from filter import Filter
from filter_diagram import Diagram


class Selector(object):

    def __init__(self, ft, ng, n):
        self.ft_constraint = ft
        self.ng_constraint = ng
        self.load_data()
        # self.constrain_ft()
        self.constrain_ng_multiple(n)
        # self.make_best_multiple()

    def load_data(self):
        self.data = np.loadtxt('data.txt')

    def constrain_ft(self):
        new = []
        for f in self.data:
            if 1 > f[1] > self.ft_constraint:
                new.append(f)
        new = sorted(new, key=lambda x: x[2])
        print(new[-1])
        self.best_chrom = new[-1]

    def constrain_ng(self):
        new = []
        for f in self.data:
            if f[2] > self.ng_constraint and f[1] != 1:
                new.append(f)
        new = sorted(new, key=lambda x: x[1])
        print(new[-1])
        best_filter = new[-1]
        self.best_chrom = []
        for i, gene in enumerate(best_filter[4:]):
            if i == 0:
                self.best_chrom.append(float(gene))
            else:
                self.best_chrom.append(int(gene))

    def constrain_ng_multiple(self, n):
        new = []
        for f in self.data:
            if f[2] > self.ng_constraint and f[1] != 1:
                new.append(f)
        new = sorted(new, key=lambda x: x[1])
        # print(new[-1])
        best_filters = new[-n:]
        self.best_chroms = []
        for fil in best_filters:
            best_chrom = []
            for i, gene in enumerate(fil[4:]):
                if i == 0:
                    best_chrom.append(float(gene))
                else:
                    best_chrom.append(int(gene))
            self.best_chroms.append(best_chrom)
        for i, fil in enumerate(best_filters):
            m = [int(i)+1 for i in fil[-10:]]
            print(m)
            Diagram(m, 'filter{}'.format(i), fil[1], fil[2])
        for i, j in zip(self.best_chroms, best_filters):
            print(i)
            print('FT Ratio: {}'.format(j[1]))
            print('NG Ratio: {}\n'.format(j[2]))

    def print_stats(self):
        pass

    def make_best(self):
        self.best = Filter(1, self.best_chrom)
        self.best.write()

    def make_best_multiple(self):
        for i, ch in enumerate(self.best_chroms):
            self.best = Filter(i+1, ch)
            self.best.write()


if True:
    Selector(0.9, 1, 30)
