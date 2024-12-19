import sys

num_list = sorted(list(map(int, sys.stdin.readline().strip().split())))

print(num_list[0] * num_list[1] + num_list[2] * num_list[3])
