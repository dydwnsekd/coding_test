"""
import sys

difficult = []
n = int(sys.stdin.readline().strip())

for _ in range(n):
    difficult.append(int(sys.stdin.readline().strip()))

if min(difficult) == difficult[0]:
    print("ez")
elif max(difficult) == difficult[0]:
    print("hard")
else:
    print("?")
"""

import sys

n = int(sys.stdin.readline())
first = int(sys.stdin.readline())

min_val = first
max_val = first

for _ in range(n - 1):
    x = int(sys.stdin.readline())
    if x < min_val:
        min_val = x
    if x > max_val:
        max_val = x

if min_val == first:
    print("ez")
elif max_val == first:
    print("hard")
else:
    print("?")

