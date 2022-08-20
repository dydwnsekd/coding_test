from collections import defaultdict
import sys

n = int(sys.stdin.readline())
num_dict = defaultdict(int)

for _ in range(n):
    num_dict[int(sys.stdin.readline())] += 1

num_list = sorted(num_dict.items())

for k, v in num_list:
    for i in range(num_dict[k]):
        print(k)
