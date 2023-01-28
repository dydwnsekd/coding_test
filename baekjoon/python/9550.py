import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    result = 0
    N, T = list(map(int, sys.stdin.readline().split()))
    candy_count = list(map(int, sys.stdin.readline().split()))

    for candy in candy_count:
        result += candy // T

    print(result)
