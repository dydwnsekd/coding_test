import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    x1, y1, f1, x2, y2, f2 = map(int, sys.stdin.readline().split())

    print(abs(x1-x2) + abs(y1-y2) + f1 + f2)
