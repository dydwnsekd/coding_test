"""
import sys

t = int(sys.stdin.readline())

def sum_dice(n, f, m):
    result = []
    for i in range(n*1+m, n*f+m+1):
        result.append(i)

    return result

for i in range(t):
    b, n ,f, m = map(int, sys.stdin.readline().split())

    if b in sum_dice(n, f, m):
        print('YES')
    else:
        print('NO')
"""

import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    b, n, f, m = map(int, sys.stdin.readline().strip().split())

    min_sum = n + m
    max_sum = n * f + m

    print("YES" if min_sum <= b <= max_sum else "NO")
