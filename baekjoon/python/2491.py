import sys

n = int(sys.stdin.readline())
length = 1
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
        else:
            if length < asc_length:
                length = asc_length
            asc_length = 1
        pre_value = i

    pre_value = num_list[0]
    for i in num_list[1:]:
        if i <= pre_value:
            desc_length += 1
        else:
            if length < desc_length:
                length = desc_length
            desc_length = 1
        pre_value = i

if asc_length > length:
    length = asc_length
elif desc_length > length:
    length = desc_length

print(length)
