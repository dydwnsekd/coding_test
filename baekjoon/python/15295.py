import sys

cases = int(sys.stdin.readline())

for i in range(cases):
    result = 0
    n, days = list(map(int, sys.stdin.readline().split()))

    for d in range(days):
        result += d+2

    print(i+1, result)
