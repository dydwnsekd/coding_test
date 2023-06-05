import sys

length_list = list(map(int, sys.stdin.readline().split()))
length_list.sort()

if length_list[0] == length_list[2]:
    print(length_list[0] * 3)
elif length_list[0] + length_list[1] <= length_list[2]:
    print(length_list[0] + length_list[1] + (length_list[0] + length_list[1] - 1))
else:
    print(sum(length_list))
