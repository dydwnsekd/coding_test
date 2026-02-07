import sys
import math

w, h = map(int, sys.stdin.readline().strip().split())
r = int(sys.stdin.readline())

print(round((w * h) - ((r ** 2) * math.pi / 4 ), 2))
