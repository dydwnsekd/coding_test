import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N, D = list(map(int, sys.stdin.readline().split()))
    count = 0
    for _ in range(N):
        v, f, c = list(map(int, sys.stdin.readline().split()))
        if float(v) * (f / c) >= D:
            count += 1

    print(count)

