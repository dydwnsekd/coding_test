import sys

num_list = [int(sys.stdin.readline())]

for i in range(9):
    temp = int(sys.stdin.readline())
    num_list.append(num_list[i] + temp)

result = 101

for i in range(len(num_list)):
    if abs(100 - num_list[i]) <= result:
        result = abs(100 - num_list[i])
        result_index = i

print(num_list[result_index])


