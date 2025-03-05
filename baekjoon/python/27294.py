import sys

t, s = map(int, sys.stdin.readline().strip().split())

if t <= 11 or 16 < t <= 23 or s == 1:
    print("280")
else:
    print("320")
