import sys

alpha_dict = {}

for i in range(65, 91):
    alpha_dict[chr(i)] = 0

s = sys.stdin.readline().strip().upper()

for i in s:
    alpha_dict[i] = alpha_dict[i] + 1

sorted_list = sorted(alpha_dict.items(), key=lambda x: x[1], reverse=True)
max_value = sorted_list[0][1]

if max_value == sorted_list[1][1]:
    print("?")
else:
    print(sorted_list[0][0])
