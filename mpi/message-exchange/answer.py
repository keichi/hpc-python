from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    comm.send({"rank": rank}, dest=1)
    msg = comm.recv(source=1)
elif rank == 1:
    msg = comm.recv(source=0)
    comm.send({"rank": rank}, dest=0)

print(f"I'm rank {rank}. Received message is: {msg}")
