import sys

n, m, k = list(map(int, sys.stdin.readline().split()))

if n - m * k > 0:
    min_value = n - m * k
else:
    min_value = 0

max_value = n - m * (k -1) - 1

print(min_value, max_value)
