import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    x, y = map(int, sys.stdin.readline().split())

    for j in range(y):
        print("X" * x)
    print()