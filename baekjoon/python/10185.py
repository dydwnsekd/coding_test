import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    p, q = list(map(int, sys.stdin.readline().split()))
    f = round(1/(1/p + 1/q), 1)
    print("f =", f)
