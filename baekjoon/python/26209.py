import sys

num_list = list(map(int, sys.stdin.readline().split()))

if num_list.count(9) > 0:
    print("F")
else:
    print("S")
