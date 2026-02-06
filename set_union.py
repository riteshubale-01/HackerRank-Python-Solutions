n = int(input())
roll_no = set(map(int, input().split()))
a = int(input())
french = set(map(int, input().split()))
A = roll_no.union(french)
mx1 = max(roll_no)
mx2 = max(french)
mx = max(mx1, mx2)
count = 0
for i in range(1,mx+1):
    if i in A:
        count += 1
print(count)
