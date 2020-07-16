import sys

n = int(sys.stdin.readline())
length = 0
asc_length = 1
desc_length = 1
equal_length = 0
pre_value = None
flag = None     # True = 커지고 있을 때, False = 작아지고 있을 때

num_list = list(map(int, sys.stdin.readline().split(" ")))

pre_value = num_list[0]

if n <= 2:
    length = n

else:
    for i in num_list[1:]:
        if pre_value < i:
            asc_length += 1

            if desc_length > length:
                length = desc_length
            desc_length = 1

        elif pre_value == i:
            asc_length += 1
            desc_length += 1

        else:
            desc_length += 1

            if asc_length > length:
                length = asc_length
            asc_length = 1
        pre_value = i
    
if asc_length > length:
    length = asc_length
elif desc_length > length:
    length = desc_length

print (length)