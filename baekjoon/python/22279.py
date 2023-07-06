import sys

cases = int(sys.stdin.readline())
qaly = 0

for _ in range(cases):
    q, y = map(float, sys.stdin.readline().split())
    qaly += q * y

print("{:.3f}".format(qaly))

