import sys

n, w, h, l = map(int, sys.stdin.readline().strip().split())

if w * h // l ** 2 > n:
    print(n)
else:
    print(w * h // l ** 2)

