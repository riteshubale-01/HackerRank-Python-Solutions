import numpy

coeff = list(map(float, input().split()))
x = float(input())

result = numpy.polyval(coeff, x)
print(result)
