import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    n, s = map(int, sys.stdin.readline().split())
    max_time = max(map(int, sys.stdin.readline().split()))

    print((s * max_time // 1000) + 1)
