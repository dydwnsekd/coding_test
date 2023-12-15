import sys
import math

cases = int(sys.stdin.readline())

for _ in range(cases):
    n, c = list(map(int, sys.stdin.readline().split()))
    print(math.ceil(n/c))
