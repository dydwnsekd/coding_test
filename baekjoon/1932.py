import sys

floor = int(sys.stdin.readline())
num_list = list()
result_list = [ [0] * i for i in range(floor, 0, -1)]

for i in range(floor):
    num_list.append(list(map(int, sys.stdin.readline().split(" "))))

num_list.reverse()

result_list[0] = num_list[0]

for i in range(1, floor):
    for j in range(0, floor-i):
        result_list[i][j] = max(result_list[i-1][j], result_list[i-1][j+1]) + num_list[i][j]

print(result_list[floor-1][0])
