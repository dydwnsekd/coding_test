"""
3 1000 2 3
200
0 2 2
300
27 3 20
"""

import sys

n, b, h, w = list(map(int, sys.stdin.readline().split()))
minimum_value = sys.maxsize

for _ in range(h):
    h_value = int(sys.stdin.readline())
    possible_w = list(map(int, sys.stdin.readline().split()))
    if max(possible_w) >= n:
        if h_value <= n * b and minimum_value > n * b:
            minimum_value = n * b

if minimum_value == sys.maxsize:
    print("stay home")
else:
    print(minimum_value)

