# TODO
# https://yiyj1030.tistory.com/490
# https://degurii.tistory.com/158
import sys
import math

one_list = [0] * 60

for i in range(1, 60):
    one_list[i] = 2 ** (i-1) + 2 * one_list[i-1]

def count_one(num):
    result = 0
    bin_num = bin(num)[2:]
    length = len(bin_num)

    for i in range(length):
        if bin_num[i] == '1':
            pow = length - i - 1
            result = one_list[pow]
            result += num - 2 ** pow + 1
            num = num - 2 ** pow

    return result


start_num, end_num = map(int, sys.stdin.readline().split())

print(count_one(end_num) - count_one(start_num-1))
