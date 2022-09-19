import sys

n = int(sys.stdin.readline())

for _ in range(n):
    r, e, c = list(map(int, sys.stdin.readline().split()))

    if r > e-c:
        print("do not advertise")
    elif r == e-c:
        print("does not matter")
    elif r < e-c:
        print("advertise")
