import sys
import math

m, d = map(int, sys.stdin.readline().strip().split())

print(math.ceil(d / m))
