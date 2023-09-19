import sys

k = int(sys.stdin.readline())
d = list(map(int, sys.stdin.readline().split()))
d1 = max(d)
d2 = min(d)

print(k**2 - ((d1-d2)/2)**2)
