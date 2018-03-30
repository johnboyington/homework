from core import Core
from parameters import Parameters
from numpy.random import rand, randint


class Operations(object):

    def __init__(self):
        self.params = Parameters()

    def splice(self, child_ID, parent_1, parent_2):
        assert isinstance(parent_1, Core), 'splicing requires Core objects'
        assert isinstance(parent_2, Core), 'splicing requires Core objects'
        child_chrom = []
        for genome in range(len(parent_1.chromosome)):
            if rand() > 0.5:
                child_chrom += [parent_1.chromosome[genome]]
            else:
                child_chrom += [parent_2.chromosome[genome]]
        return Core(child_ID, child_chrom)

    def mutate(self, individual):
        gene = randint(0, self.params.num_disc)
        assert isinstance(individual, Core), 'mutating requires Core objects'
        new_gene = randint(0, self.params.num_mat - 1)
        chrom = individual.chromosome
        chrom[gene] = new_gene
        return Core(individual.ID, chrom)

ops = Operations()
