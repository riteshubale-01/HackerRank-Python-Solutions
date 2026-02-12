import numpy

n, m = map(int, input().split())

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

arr = numpy.array(matrix, int)
print (numpy.transpose(arr))
print (arr.flatten())
