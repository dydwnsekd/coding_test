#TODO
import sys

num_count, result_value = list(map(int, sys.stdin.readline().split(" ")))
num_list = list(map(int, sys.stdin.readline().split(" ")))

result_list = [[0] * i for i in range(1, num_count+1)]
final_list = list()
count = 0 

for i in range(num_count):
    result_list[i][i] = num_list[i]

for i in range(1, num_count):
    for j in range(i):
        result_list[i][j] = result_list[i-1][j] + num_list[i]

for i in range(num_count):
    final_list.extend(result_list[i])

for i in final_list:
    if i == result_value:
        count += 1

print (result_list)
print(count)
    