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

def count_one(n):
    count = 0
    while n:
        n &= n-1
        count += 1
    return count

start_num, end_num = map(int, sys.stdin.readline().split(" "))

count = 0

for i in range(start_num, end_num+1):
    count += count_one(i)

print(count)


