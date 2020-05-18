import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

send_buf = np.full(100000, rank, dtype=np.int)
recv_buf = np.zeros(100000, dtype=np.int)

if rank == 0:
    comm.Send(send_buf, dest=1)
    comm.Recv(recv_buf, source=1)
elif rank == 1:
    comm.Recv(recv_buf, source=0)
    comm.Send(send_buf, dest=0)

print(f"I'm rank {rank}. Received rank is: {recv_buf[0]}")
