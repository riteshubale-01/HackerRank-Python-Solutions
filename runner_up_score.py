if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

r = sorted(arr, reverse = True)
s = list(set(r))
print(s[1])
