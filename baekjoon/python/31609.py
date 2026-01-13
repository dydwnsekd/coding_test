"""
import sys

n = int(sys.stdin.readline())
num_list = list(set(map(int, sys.stdin.readline().strip().split())))
num_list.sort()

for n in num_list:
    print(n)
"""

import sys

_ = int(sys.stdin.readline().strip())
unique_numbers = sorted(set(map(int, sys.stdin.readline().strip().split())))

for value in unique_numbers:
    print(value)

