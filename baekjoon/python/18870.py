import sys
from collections import Counter

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
num_rank = sorted(num_list)

for num in num_list:
    print(num_rank.index(num), end=" ")
