from itertools import product

a = list(set(map(int, input().split())))
b = list(set(map(int, input().split())))

t = tuple(product(a, b))
for x in t:
    print(x, end=' ')
