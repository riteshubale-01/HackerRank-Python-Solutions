if __name__ == '__main__':
    n = int(input())
    ls = []
    for _ in range(n):
        command, *line = input().split()
        if command == 'insert':
            ls.insert(int(line[0]), int(line[1]))
        elif command == 'remove':
            ls.remove(int(line[0]))
        elif command == 'append':
            ls.append(int(line[0]))
        elif command == 'pop':
            ls.pop()
        elif command == 'print':
            print(ls)
        elif command == 'sort':
            ls.sort()
        elif command == 'reverse':
            ls.reverse()