import sys

value = 0

x, y, z = map(int, sys.stdin.readline().strip().split())
u, v, w = map(int, sys.stdin.readline().strip().split())

value += (u / 100) * x
value += (v / 50) * y
value += (w / 20) * z

print(int(value))

