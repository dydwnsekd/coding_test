import sys
from itertools import combinations

n, m = list(map(int, sys.stdin.readline().split()))
num_list = list(map(int, sys.stdin.readline().split()))

sum_list = list(map(sum, list(combinations(num_list, 3))))

print(sum_list)
