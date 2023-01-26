import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    N, D = list(map(int, sys.stdin.readline().split()))
    result = 0

    for _ in range(N):
        v, f, c = list(map(int, sys.stdin.readline().split()))
        if v * (f/c) >= D:
            result += 1
    print(result)
