import sys

n = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split(" ")))

num_list.sort()

print("%d %d" % (num_list[0], num_list[-1]))