"""
import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))

min_n = min(n_list)
min_index = n_list.index(min_n)

print(min_index)
"""

import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

min_index, min_val = min(enumerate(nums), key=lambda x: x[1])
print(min_index)
