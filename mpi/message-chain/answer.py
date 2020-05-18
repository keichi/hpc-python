import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

send_buf = np.full(100000, rank, dtype=np.int)
recv_buf = np.zeros(100000, dtype=np.int)

if rank > 0:
    comm.Recv(recv_buf, source=rank-1)
    print(f"I'm rank {rank} received {recv_buf[0]} from rank {rank-1}")

if rank < size - 1:
    print(f"I'm rank {rank} sending {send_buf.size} elements to rank {rank+1}")
    comm.Send(send_buf, dest=rank+1)

source = rank - 1
dest = rank + 1

if rank == 0:
    source = MPI.PROC_NULL
if rank == size - 1:
    dest = MPI.PROC_NULL

comm.Sendrecv(send_buf, dest=dest, recvbuf=recv_buf, source=source)

print(f"I'm rank {rank} sent message to {dest} and received from {source}")
