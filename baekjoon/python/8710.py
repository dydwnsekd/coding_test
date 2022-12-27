import sys

k, w, m = list(map(int, sys.stdin.readline().split()))
count = 0

if w-k <= 0:
    print(0)
else:
    if (w-k) % m == 0:
        print((w-k) // m)
    else:
        print(((w-k) // m) + 1)
