from parallel_cycle import Cycle
from slave import slave
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


class Driver(object):

    def __init__(self):
        if rank == 0:
            Cycle()
        else:
            done = comm.recv(source=0, tag=rank)
            while not done:
                slave()
                done = comm.recv(source=0, tag=rank)


if __name__ == '__main__':
    Driver()
