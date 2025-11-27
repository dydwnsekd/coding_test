"""
import sys
import math

n, s = map(int, sys.stdin.readline().strip().split())

solve_time = max(map(int, sys.stdin.readline().strip().split()))

print(math.ceil(solve_time * s / 1000))
"""

import sys
import math

n, s = map(int, sys.stdin.readline().strip().split())
max_time = 0

for t in map(int, sys.stdin.readline().strip().split()):
    if t > max_time:
        max_time = t

print(math.ceil(max_time * s / 1000))
