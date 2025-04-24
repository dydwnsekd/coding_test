import sys

value_list = [1, 5, 10, 20, 50, 100][::-1]
dollar_list = list(map(int, sys.stdin.readline().strip().split(' ')))[::-1]

bag_value = []

for i in range(len(dollar_list)):
    bag_value.append(dollar_list[i] * value_list[i])

max_index = bag_value.index(max(bag_value))
print(value_list[max_index])

