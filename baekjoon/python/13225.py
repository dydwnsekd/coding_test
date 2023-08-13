import sys
import math

def get_divisor(num):

    divisor_list = []
    if num ==1:
        return [1]
    elif num == 2:
        return [1, 2]
    elif num == 3:
        return [1, 3]

    for i in range(1, num//2 + 1):
        if num % i == 0:
            divisor_list.append(i)
            divisor_list.append(num // i)

    divisor_list = list(set(divisor_list))
    divisor_list.sort()
    return divisor_list


cases = int(sys.stdin.readline())

for _ in range(cases):
    temp = int(sys.stdin.readline())
    print(temp, len(get_divisor(temp)))
