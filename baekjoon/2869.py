import sys
import math

A, B, V = map(int, sys.stdin.readline().split(' '))

height = A
day = 1

day += math.ceil((V-A) / (A-B))

print (day)
