from population import Population
from time import time


class Test_Cycle(object):

    def __init__(self, start_size, num_gens):
        start_time = time()
        self.start_size = start_size
        self.num_generations = num_gens
        self.iterate()
        self.total_time = time() - start_time
        self.write_info()

    def iterate(self):
        self.origin()
        for i in range(self.num_generations):
            self.cycle()
        self.test.store_best_core()

    def origin(self):
        self.test = Population(self.start_size, store_all=True)
        self.test.init_current_gen()
        self.test.run_current_gen()
        self.test.sort_current_gen()
        self.test.store_current_gen()

    def cycle(self):
        self.test.init_next_gen()
        self.test.run_current_gen()
        self.test.sort_current_gen()
        self.test.store_current_gen()
        self.test.store_best_filter()

    def write_info(self):
        s = 'Total Run Time: {}\n'.format(self.total_time)
        s += 'Starting Gen Size: {}'.format(self.start_size)
        with open('info.txt', 'w+') as F:
            F.write(s)

    def plot(self):
        self.test.plot_legacy()


if __name__ == '__main__':
    test = Test_Cycle(4, 2)
