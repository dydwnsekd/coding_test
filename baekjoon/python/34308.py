"""
import sys

n, k = map(int, sys.stdin.readline().strip().split())
apple_list = list(map(int, sys.stdin.readline().strip().split()))

for apple in apple_list:
    if abs(apple - 1) > abs(apple - n):
        print(n, end=" ")
    else:
        print(1, end=" ")
"""

import sys

n, k = map(int, sys.stdin.readline().strip().split())
apples = list(map(int, sys.stdin.readline().strip().split()))

out = []
for a in apples:
    dist_to_1 = abs(a - 1)
    dist_to_n = abs(a - n)
    out.append(str(n if dist_to_n < dist_to_1 else 1))

print(" ".join(out))

