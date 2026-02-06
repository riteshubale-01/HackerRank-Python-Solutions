if __name__ == '__main__':
    students = []
    n = int(input())
    for _ in range(n):
        name = input()
        score = float(input()) 
        students.append([name, score])
    mn = min(student[1] for student in students)
    students = [student for student in students if student[1] != mn]
    mn2 = min(student[1] for student in students)
    ls = []
    for i, student in enumerate(students):
        if student[1] == mn2:
            ls.append(student[0])
    ls.sort()
    for word in ls:
        print(word)