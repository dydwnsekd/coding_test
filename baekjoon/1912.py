import sys

num_count = int(sys.stdin.readline())
input_num = list(map(int, sys.stdin.readline().split(" ")))

result_list = [0 for i in range(num_count)]
result_list[0] = input_num[0]

max_value = input_num[0]

for i in range(1, num_count):

    if result_list[i-1] + input_num[i] < input_num[i]:
        result_list[i] = input_num[i]
    else:
        result_list[i] = result_list[i-1] + input_num[i]

    if max_value < result_list[i]:
        max_value = result_list[i]    

print (max_value)
    