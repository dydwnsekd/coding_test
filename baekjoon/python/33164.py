"""
import sys

result = 0
n, m = map(int, sys.stdin.readline().strip().split())

a_list = list(map(int, sys.stdin.readline().strip().split()))
b_list = list(map(int, sys.stdin.readline().strip().split()))

for a in a_list:
    for b in b_list:
        result += (a+b) * max(a, b)

print(result)
"""

import sys
import bisect

n, m = map(int, sys.stdin.readline().strip().split())
A = sorted(map(int, sys.stdin.readline().strip().split()))
B = sorted(map(int, sys.stdin.readline().strip().split()))

prefix_B = [0]
for x in B:
    prefix_B.append(prefix_B[-1] + x)

sum_B = prefix_B[-1]
result = 0

for a in A:
    idx = bisect.bisect_right(B, a)
    sum_b_le = prefix_B[idx]
    sum_b_gt = sum_B - sum_b_le
    cnt_gt = m - idx

    result += idx * (a * a) + a * sum_b_le
    result += a * sum_b_gt + sum(b * b for b in B[idx:])

print(result)
