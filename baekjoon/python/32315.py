import sys

num_list = []
phone_num = sys.stdin.readline().strip()

for i in phone_num:
    if i not in num_list:
        num_list.append(i)

print(len(num_list) - 1)
