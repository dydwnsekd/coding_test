import sys

num_list = list(map(int, sys.stdin.readline().strip().split()))

num_list.sort()

print(2 * num_list[2] - sum(num_list[:2]))
