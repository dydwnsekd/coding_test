import sys

t = int(sys.stdin.readline())

for _ in range(t):
    result = 0
    d = int(sys.stdin.readline())

    for i in range(1, d):
        if i + i ** 2 <= d:
            result = i
        else:
            break

    print(result)
