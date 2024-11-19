import sys

num_list = [int(sys.stdin.readline())]

for i in range(9):
    temp = int(sys.stdin.readline())
    num_list.append(num_list[i] + temp)

result = 100
print(num_list)

for i in range(len(num_list)):
    if 100 - num_list[i] < result:
        result = 100 - num_list[i]
        result_index = i

print(num_list[result_index])


