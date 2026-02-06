m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))
result = sorted(a.symmetric_difference(b))
result = list(result)
for num in result:
    print(num)