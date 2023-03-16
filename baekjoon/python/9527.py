# TODO
import sys
import math

def to_binary(n):

    binary_list = list()
    
    while n > 1:
        if math.floor(n % 2) == 1:
            binary_list.insert(0, '1')
        elif math.floor(n % 2) == 0:
            binary_list.insert(0, '0')
        n = math.floor(n / 2)

    binary_list.insert(0, str(n))
    return str(int(''.join(binary_list)))


start_num, end_num = map(int, sys.stdin.readline().split(" "))

count = 0

for i in range(start_num, end_num+1):
    temp = to_binary(i)
    count += temp.count("1")

print(count)


