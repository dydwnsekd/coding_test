import sys

a, b = map(int, sys.stdin.readline().split())

if a == b:
    print(a)
elif a > b:
    print(a)
else:
    print(b)
