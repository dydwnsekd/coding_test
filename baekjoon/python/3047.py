'''
import sys

num_list = list(map(int, sys.stdin.readline().strip().split()))
sort_str = sys.stdin.readline().strip()

num_list.sort()

for s in sort_str:
    if s == "A":
        print(num_list[0], end=" ")
    elif s == "B":
        print(num_list[1], end=" ")
    elif s == "C":
        print(num_list[2], end=" ")
'''

import sys

num_list = sorted(map(int, sys.stdin.readline().strip().split()))
sort_str = sys.stdin.readline().strip()

order_map = {'A': 0, 'B': 1, 'C': 2}

print(" ".join(str(num_list[order_map[char]]) for char in sort_str))
