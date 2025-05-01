import sys, math

a, b, h, w = map(int, sys.stdin.readline().strip().split())

print(math.ceil(h/a) * math.ceil(w/b))
