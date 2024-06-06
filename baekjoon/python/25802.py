import sys

sequence = 3

start_num = list(map(int, sys.stdin.readline().split()))
current_num_list = start_num.copy()

while True:
    current_num = sum(current_num_list) % 10
    current_num_list.pop(0)
    current_num_list.append(current_num)

    if start_num == current_num_list:
        break

    sequence += 1

print(sequence)

