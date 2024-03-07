import sys

x, y = map(int, sys.stdin.readline().split())

if x > y:
    print(x+y)
elif x == y:
    print(y)
else:
    print(y-x)
