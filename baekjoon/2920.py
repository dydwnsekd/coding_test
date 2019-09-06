import sys

num_list = list(map(int, sys.stdin.readline().split(" ")))
flag = None

if num_list[0] == 1:
    for i in range(1, len(num_list)):
        if num_list[i] - num_list[i-1] == 1:
            flag = 1
        else:
            flag = 0
            break

elif num_list[0] == 8:
    for i in range(1, len(num_list)):
        if num_list[i] - num_list[i-1] == -1:
            flag = -1
        else:
            flag = 0
            break

if flag == 1:
    print("ascending")
elif flag == -1:
    print("descending")
else:
    print("mixed")
        