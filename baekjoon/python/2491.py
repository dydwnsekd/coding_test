#TODO
import sys

n = int(sys.stdin.readline())
length = 0
asc_length = 1
desc_length = 1
equal_count = 0
pre_value = None
flag = None     # True = 커지고 있을 때, False = 작아지고 있을 때

num_list = list(map(int, sys.stdin.readline().strip().split(" ")))

pre_value = num_list[0]

if n <= 2:
    length = n

else:
    for i in num_list[1:]:
        if pre_value < i:
            asc_length += 1

            if desc_length > length:
                length = desc_length + equal_count
            desc_length = 1
            equal_count = 0

        elif pre_value == i:
            equal_count += 1

        else:
            desc_length += 1

            if asc_length > length:
                length = asc_length + equal_count
            asc_length = 1
            equal_count = 0

        pre_value = i

if asc_length > length:
    length = asc_length + equal_count
elif desc_length > length:
    length = desc_length + equal_count

print(length)
