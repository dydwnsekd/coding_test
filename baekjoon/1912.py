import sys

max_value = -999999999

num_count = int(sys.stdin.readline())
input_num = list(map(int, sys.stdin.readline().split(" ")))

for i in range(num_count):
    result_list = [0 for i in range(num_count)]
    for j in range(i, num_count):
        #print (j)
        result_list[j] = result_list[j-1] + input_num[j]

    if max(result_list) > max_value:
        max_value = max(result_list)

print (max_value)
    