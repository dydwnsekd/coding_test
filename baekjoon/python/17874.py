import sys

n, h, v = list(map(int, sys.stdin.readline().split()))
result = 1

if h > n-h:
    result *= h
else:
    result *= (n-h)

if v > n-v:
    result *= v
else:
    result *= (n-v)

print(result * 4)
