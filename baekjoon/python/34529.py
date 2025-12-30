import sys

x, y, z = map(int, sys.stdin.readline().strip().split())
u, v, w = map(int, sys.stdin.readline().strip().split())

value = (u * x) / 100 + (v * y) / 50 + (w * z) / 20

print(int(value))

