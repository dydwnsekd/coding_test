import sys

y, c, p = map(int, sys.stdin.readline().strip().split())

print(min(y, c//2, p))
