import sys
import math

A, B, C = map(int, sys.stdin.readline().split(" "))
count = 1

if B >= C:
    print (-1)
else:
    print (math.floor(A / (C - B)) + 1)