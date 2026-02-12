import numpy

n, m, p = map(int, input().split())
A = []
B = []

for _ in range(n):
    rows1 = list(map(int, input().split()))
    A.append(rows1)

for _ in range(m):
    rows2 = list(map(int, input().split()))
    B.append(rows2)
    
array_1 = numpy.array(A, int)
array_2 = numpy.array(B, int)

print(numpy.concatenate((array_1, array_2), axis = 0))
