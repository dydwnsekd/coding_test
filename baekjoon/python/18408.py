import sys

num_list = list(sys.stdin.readline().strip().split())

if num_list.count("1") > num_list.count("2"):
    print(1)
else:
    print(2)
