from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


def slave():
    chunk = comm.recv(source=0, tag=rank)
    for ind in chunk:
            if ind.fitness == -1:
                ind.run_local()
    comm.send(chunk, dest=0, tag=rank)
    return
