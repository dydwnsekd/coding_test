from collections import Counter

import sys

n = int(sys.stdin.readline())
num_list = []

for _ in range(n):
    num_list.append(int(sys.stdin.readline()))

num_dict = Counter(num_list)
num_list = sorted(num_dict.items())

for n_count in num_list:
    num = n_count[0]
    count = n_count[1]
    for _ in range(count):
        print(num)
