import sys

num_list = list(map(int, sys.stdin.readline().strip().split()))
num_list = sorted(num_list)

if num_list[0] + num_list[1] == num_list[2]:
    print(1)
elif num_list[0] * num_list[1] == num_list[2]:
    print(2)
else:
    print(3)
