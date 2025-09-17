import sys

x, y = map(int, sys.stdin.readline().split())
print(min(x + y, 2 * min(x, y) + 1))
