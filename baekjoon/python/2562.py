import sys

num_list = list()

for _ in range(9):
    num_list.append(int(sys.stdin.readline()))

max_value = max(num_list)

print(max_value)
print(num_list.index(max_value)+1)