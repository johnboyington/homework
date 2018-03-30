from core import Core
from parameters import Parameters
from numpy.random import rand, randint
import numpy as np
from operations import ops
# import matplotlib.pyplot as plt
import copy
# comm = MPI.COMM_WORLD
# rank = comm.Get_rank()
# size = comm.Get_size()


class Population(object):

    def __init__(self, initial_pop, store_all):
        self.initial_population = initial_pop
        self.params = Parameters()
        self.current_generation = []
        self.historic_population = 0
        self.next_generation = []
        self.store_all = store_all
        if self.store_all:
            self.store_all
            self.legacy = []

    def spawn_random(self, ID):
        chrom = []
        for mat in range(self.params.num_disc):
            chrom += [randint(0, self.params.num_mat)]
        return Core(ID, chrom)

    def init_current_gen(self):
        for i in range(self.initial_population):
            self.current_generation += [self.spawn_random(self.historic_population)]
            self.historic_population += 1

    def divide_work(self):
        work = []
        prev = []
        new = []
        for ind in self.current_generation:
            if ind.fitness == -1:
                work.append(ind)
            else:
                prev.append(ind)
        rate = (len(work) // size) + 1
        for ind in range(1, size):
            l = (ind-1) * rate
            r = (ind) * rate
            chunk = work[l:r]
            comm.send(chunk, dest=ind, tag=ind)
        # do own work
        last_index = (size - 1) * rate
        new = work[last_index:]
        for ind in new:
            ind.run_local()
        for ind in range(1, size):
            new += comm.recv(source=ind, tag=ind)
        self.current_generation = prev + new

    def run_current_gen(self):
        for ind in self.current_generation:
            if ind.fitness == -1:
                ind.run_local()

    def sort_current_gen(self):
        self.current_generation = sorted(self.current_generation, key=Core.get_fitness)
        self.best_filter = self.current_generation[-1]
        self.legacy.append(copy.deepcopy(self.current_generation))
        if len(self.current_generation) > self.params.max_population:
            self.current_generation = self.current_generation[-self.params.max_population:]
        # calculate CDF
        pdf = []
        for i in self.current_generation:
            pdf.append(i.fitness)
        pdf = np.array(pdf)
        pdf = pdf / np.sum(pdf)
        cdf = []
        for i, p in enumerate(pdf):
            cdf.append(np.sum(pdf[:i+1]))
        self.cdf = cdf

    def store_current_gen(self):
        s = ''
        for i in self.current_generation:
            args = i.fitness, i.eol_burnup, i.max_pppf, i.max_k_inf
            s += '{:10.6f}  {:10.6f}  {:10.6f}  {:10.6f}  '.format(*args)
            arr = np.array(i.chromosome)
            for m in arr:
                s += '  {:3d}'.format(m)
            s += '\n'
        with open('data.txt', 'a+') as F:
            F.write(s)

    def store_best_core(self):
        best = self.best_filter
        s = ''
        args = best.fitness, best.eol_burnup, best.max_pppf, best.max_k_inf
        s += '{:10.6f}  {:10.6f}  {:10.6f}  {:10.6f}  '.format(*args)
        arr = np.array(best.chromosome)
        for m in arr:
            s += '  {:3d}'.format(m)
        s += '\n'
        with open('best_core.txt', 'a+') as F:
            F.write(s)

    def select(self):
        r1 = rand()
        r2 = rand()
        found_1 = False
        found_2 = False
        for i, ind in enumerate(self.cdf):
            if r1 < ind and not found_1:
                parent_1 = self.current_generation[i]
                found_1 = True
            if r2 < ind and not found_2:
                parent_2 = self.current_generation[i]
                found_2 = True
            if found_1 and found_2:
                break
        return parent_1, parent_2

    def init_next_gen(self):
        self.next_generation = []
        for i in range(self.params.next_gen_size):
            self.next_generation += [ops.splice(self.historic_population, *self.select())]
            self.historic_population += 1
        for i in range(self.params.mut_per_gen):
            lucky = randint(0, len(self.next_generation) - 1)
            self.next_generation[lucky] = ops.mutate(self.next_generation[lucky])
        self.current_generation += self.next_generation
        return

    def plot_current_gen(self):
        ids = range(len(self.current_generation))
        fitnesses = []
        for i in ids:
            fitnesses.append(self.current_generation[i].fitness)
        plt.figure(10)
        plt.plot(ids, fitnesses, 'ko')
        plt.show()

    def plot_legacy(self):
        ids = range(len(self.current_generation))
        plt.figure(20)
        plt.xlabel('individual')
        plt.ylabel('fitness')
        for n, l in enumerate(self.legacy):
            fitnesses = []
            for i in ids:
                fitnesses.append(l[i].fitness)
                plt.plot(ids, fitnesses, linestyle='None', marker='o', label='gen {}'.format(n))
        plt.legend()
        plt.show()


if __name__ == '__main__':
    test = Population(4)
    test.init_current_gen()
    test.run_current_gen()
    test.sort_current_gen()
    p1, p2 = test.select()
    print(p1.ID, p2.ID)
    # test.plot_current_gen()
