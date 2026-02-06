n = int(input())
ls = []
for _ in range(n):
    country = input()
    ls.append(country)
s = set(ls)
print(len(s))