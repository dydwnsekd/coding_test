import sys

w, h, d = map(int, sys.stdin.readline().strip().split())

if w <= 2 * d or h <= 2 * d:
    print(0)
else:
    print((w-2*d) * (h-2*d))
