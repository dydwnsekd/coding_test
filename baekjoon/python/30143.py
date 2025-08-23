import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, a, d = map(int, sys.stdin.readline().split())

    result = a

    for i in range(1, n):
        a += d
        result += a

    print(result)
