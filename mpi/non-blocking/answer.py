import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

send_buf = np.full(100000, rank, dtype=np.int)
recv_buf = np.zeros(100000, dtype=np.int)

source = rank - 1
dest = rank + 1

if rank == 0:
    source = MPI.PROC_NULL
if rank == size - 1:
    dest = MPI.PROC_NULL

reqs = []

reqs.append(comm.Irecv(recv_buf, source=source))
reqs.append(comm.Isend(send_buf, dest=dest))

MPI.Request.waitall(reqs)

print(f"I'm rank {rank} received {recv_buf[0]} from rank {rank-1}")
print(f"I'm rank {rank} sending {send_buf.size} elements to rank {rank+1}")
