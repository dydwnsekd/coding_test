import sys

num_list = list(map(int, sys.stdin.readline().strip().split()))
num_list.sort(reverse=True)

print(sum(num_list[:2]))
