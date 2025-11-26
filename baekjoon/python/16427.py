import sys
import math

n, s = map(int, sys.stdin.readline().strip().split())

solve_time = max(map(int, sys.stdin.readline().strip().split()))

print(math.ceil(solve_time * s / 1000))

