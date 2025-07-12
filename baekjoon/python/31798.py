import sys
import math

a, b, c = map(int, sys.stdin.readline().split())

if a == 0:
    print(c ** 2 - b)
elif b == 0:
    print(c ** 2 - a)
elif c == 0:
    print(int(math.sqrt(a + b)))


