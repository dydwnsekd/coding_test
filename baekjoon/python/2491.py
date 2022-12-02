#TODO
import sys

n = int(sys.stdin.readline())
length = 1
asc_length = 0
desc_length = 0
equal_count = 0
pre_value = None
flag = None     # True = 커지고 있을 때, False = 작아지고 있을 때

num_list = list(map(int, sys.stdin.readline().strip().split(" ")))

pre_value = num_list[0]

if n <= 2:
    length = n

else:
    for i in num_list[1:]:
        if i >= pre_value:
            asc_length += 1
        else:
            if length < asc_length + 1:
                length = asc_length + 1
                asc_length = 0
        pre_value = i

    for i in num_list[1:]:
        if i <= pre_value:
            desc_length += 1
        else:
            if length < desc_length + 1:
                length = desc_length + 1
                desc_length = 0
        pre_value = i

if asc_length + 1 > length:
    length = asc_length + 1
elif desc_length + 1 > length:
    length = desc_length + 1

print(length)
