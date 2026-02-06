N = int(input())

columns = input().split()
marks_index = columns.index("MARKS")

total_marks = 0

for _ in range(N):
    data = input().split()
    total_marks += float(data[marks_index])

average = total_marks / N
print(f"{average:.2f}")