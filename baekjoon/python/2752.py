import sys

num_list = list(map(int, sys.stdin.readline().strip().split()))
num_list.sort()

print(*num_list)
