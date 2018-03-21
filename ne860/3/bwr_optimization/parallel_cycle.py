from population import Population
from time import time
from parameters import Parameters
from slave import slave
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


class Cycle(object):

    def __init__(self):
        start_time = time()
        self.params = Parameters()
        self.iterate()
        self.total_time = time() - start_time
        self.write_info()

    def iterate(self):
        self.origin()
        for i in range(self.params.num_gens):
            print('Running generation {}'.format(i + 1), flush=True)
            self.cycle()
        for ind in range(1, size):
            comm.send(True, dest=ind, tag=ind)
        self.test.store_best_filter()

    def origin(self):
        print('Initializing Population...', flush=True)
        self.test = Population(self.params.start_size, store_all=True)
        self.test.init_current_gen()
        self.parallel()
        self.test.sort_current_gen()
        self.test.store_current_gen()

    def cycle(self):
        self.test.init_next_gen()
        self.parallel()
        self.test.sort_current_gen()
        self.test.store_current_gen()
        self.test.store_best_filter()

    def parallel(self):
        for ind in range(1, size):
            comm.send(False, dest=ind, tag=ind)
        self.test.divide_work()

    def write_info(self):
        s = 'Total Run Time: {}\n'.format(self.total_time)
        total_filters = self.params.start_size * (self.params.num_gens + 1)
        s += 'Average Filter Calculation Time: {} s\n'.format(self.total_time / total_filters)
        s += 'Total Number of Filters Calculated: {}\n'.format(total_filters)
        s += 'Starting Gen Size: {}\n'.format(self.params.start_size)
        s += 'Total Generations: {}\n'.format(self.params.num_gens + 1)
        s += 'Minimum Filter Length: {}\n'.format(self.params.min_length)
        s += 'Maximum Filter Length: {}\n'.format(self.params.max_length)
        s += 'Number of Filter Discretizations: {}\n'.format(self.params.num_disc)
        with open('info.txt', 'w+') as F:
            F.write(s)

    def plot(self):
        self.test.plot_legacy()


if __name__ == '__main__':
    if rank == 0:
        test = Cycle(31, 2)
    else:
        done = comm.recv(source=0, tag=rank)
        while not done:
            slave()
            done = comm.recv(source=0, tag=rank)
