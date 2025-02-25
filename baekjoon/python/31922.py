import sys

a, p, c = map(int, sys.stdin.readline().strip().split())

if a + c > p:
    print(a + c)
else:
    print(p)
