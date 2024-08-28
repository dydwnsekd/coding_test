import sys

zero_index = []
need_num = [1, 2, 3, 4]
num_box = list(map(int, sys.stdin.readline().strip().split()))

for i in range(4):
    if num_box[i] == 0:
        zero_index.append(i)
    else:
        need_num.remove(num_box[i])

if len(zero_index) == 0:
    print(num_box[0], num_box[1])
elif len(zero_index) == 1:
    print(zero_index[0] + 1, need_num[0])
else:
    print(need_num[0], need_num[1])

