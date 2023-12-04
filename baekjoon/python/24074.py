import sys

num_count = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
max_value = max(num_list)
max_index = num_list.index(max_value)

print(sum(num_list[:max_index]))
print(sum(num_list[max_index+1:]))
