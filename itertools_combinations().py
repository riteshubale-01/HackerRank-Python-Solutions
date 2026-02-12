from itertools import combinations

s, k = input().split()
k = int(k)
for i in range(1, k + 1):
    for comb in sorted(list(combinations(sorted(s), i))):
        print("".join(comb))
