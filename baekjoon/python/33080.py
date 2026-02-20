"""
import sys

max_value = 0
balance_count = 0
n, m = map(int, sys.stdin.readline().strip().split())
score_list = sorted(list(map(int, sys.stdin.readline().strip().split())))

for i in range(len(score_list) - 2):
    if max(score_list[i:i + 3]) - min(score_list[i:i + 3]) <= m:
        balance_count += 1
        if max_value < sum(score_list[i:i + 3]):
            max_value = sum(score_list[i:i + 3])

if balance_count == 0:
    print(-1)
else:
    print(balance_count, max_value)
"""

"""
import sys
from itertools import combinations

max_value = 0
balance_count = 0
n, m = map(int, sys.stdin.readline().strip().split())
score_list = list(map(int, sys.stdin.readline().strip().split()))

for i in combinations(score_list, 3):
    if max(i) - min(i) <= m:
        balance_count += 1
        if max_value < sum(i):
            max_value = sum(i)

if balance_count == 0:
    print(-1)
else:
    print(balance_count, max_value)
"""

import sys

n, m = map(int, sys.stdin.readline().strip().split())
a = sorted(map(int, sys.stdin.readline().strip().split()))

count = 0
best_sum = 0

for i in range(n - 2):
    k = i + 2
    for j in range(i + 1, n - 1):
        if k < j + 1:
            k = j + 1

        while k < n and a[k] - a[i] <= m:
            k += 1

        if k - 1 >= j + 1:
            cnt = (k - 1) - (j + 1) + 1
            count += cnt

            s = a[i] + a[j] + a[k - 1]
            if s > best_sum:
                best_sum = s

print(-1 if count == 0 else f"{count} {best_sum}")

