import sys

a, b = map(int, sys.stdin.readline().strip().split())
c, d = map(int, sys.stdin.readline().strip().split())

print(min(a+d, b+c))

