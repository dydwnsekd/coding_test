import sys

a, b, c, d = map(int, sys.stdin.readline().strip().split())

if a + b <= d and c <= d:
    print("~.~")
elif a + b > d and c > d:
    print("T.T")
elif a + b <= d and c > d:
    print("Shuttle")
elif a + b > d and c <= d:
    print("Walk")
