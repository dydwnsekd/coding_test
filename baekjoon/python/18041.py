import sys

max_result = 1
temp = 1
n, x = map(int, sys.stdin.readline().strip().split())

viewpoint_list = list(map(int, sys.stdin.readline().strip().split()))

for i in range(len(viewpoint_list) - 1):
    if viewpoint_list[i+1] - viewpoint_list[i] <= x:
        temp += 1
    else:
        if max_result < temp:
            max_result = temp
        temp = 1

if max_result < temp:
    max_result = temp

print(max_result)
