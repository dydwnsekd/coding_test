"""
import sys

n = int(sys.stdin.readline())
result = []

for i in range(n):
    answer_list = list(map(int, sys.stdin.readline().strip().split()))

    flag = True
    for j in range(10):
        if answer_list[j] != (j % 5) + 1:
            flag = False
            break

    if flag:
        result.append(i + 1)

print('\n'.join(map(str, result)))
"""

import sys

n = int(sys.stdin.readline().strip())
results = []

pattern = [(i % 5) + 1 for i in range(10)]

for idx in range(1, n + 1):
    answers = list(map(int, sys.stdin.readline().strip().split()))
    if answers == pattern:
        results.append(idx)

print('\n'.join(map(str, results)))
