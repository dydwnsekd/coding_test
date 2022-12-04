import sys

n = int(sys.stdin.readline())
length = 0
asc_length = 1
desc_length = 1
pre_value = None

num_list = list(map(int, sys.stdin.readline().strip().split(" ")))

if n <= 2:
    length = n

else:
    pre_value = num_list[0]
    for i in num_list[1:]:
        if i >= pre_value:
            asc_length += 1
            if length < asc_length:
                length = asc_length
        else:
            asc_length = 1
        pre_value = i

    pre_value = num_list[0]
    for i in num_list[1:]:
        if i <= pre_value:
            desc_length += 1
            if length < desc_length:
                length = desc_length
        else:
            desc_length = 1
        pre_value = i

print(length)
