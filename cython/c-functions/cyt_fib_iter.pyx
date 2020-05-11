cpdef fibonacci(int n):
    if n < 2:
        return n

    cdef int a = 0
    cdef int b = 1

    for i in range(2, n + 1):
        a, b = b, a + b
        
    return b
