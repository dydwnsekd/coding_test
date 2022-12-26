import sys

k, w, m = list(map(int, sys.stdin.readline().split()))
count = 0

if w-k < 0:
    print(0)
else:
    print(((w-k) // m) + 1)
과