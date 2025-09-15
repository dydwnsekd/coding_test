import sys

x, y = map(int, sys.stdin.readline().strip().split())

if x == y:
    print(x + y)
else:
    print(min(x, y) * 2 + 1)
