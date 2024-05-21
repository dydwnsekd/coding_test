import sys

num_list = []
num_list.append(int(sys.stdin.readline()))
num_list.append(int(sys.stdin.readline()))
num_list.append(int(sys.stdin.readline()))

num_list.sort()

if num_list[0] + num_list[1] == num_list[2]:
    print(1)
else:
    print(0)
