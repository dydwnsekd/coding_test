#TODO
import sys
import math

n = int(sys.stdin.readline())
o = int(sys.stdin.readline())
result = []

min_value = math.floor(o * (n / (n-1)))
max_value = math.ceil(o * (n / (n-1)))

if min_value - o <= min_value // 2:
    result.append(min_value)
if max_value - o <= max_value // 2:
    result.append(max_value)
