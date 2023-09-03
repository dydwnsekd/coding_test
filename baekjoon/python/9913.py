import sys
from collections import Counter

num_list = Counter()
cases = int(sys.stdin.readline())

for _ in range(cases):
    num_list[int(sys.stdin.readline())] += 1

print(max(num_list.values()))
