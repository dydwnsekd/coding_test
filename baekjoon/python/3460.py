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


def to_binary_reverse(n):

    binary_list = list()
    
    while n > 1:
        if math.floor(n % 2) == 1:
            binary_list.append('1')
        elif math.floor(n % 2) == 0:
            binary_list.append('0')
        n = math.floor(n / 2)

    binary_list.append(str(n))
    return (''.join(binary_list))

n = int(sys.stdin.readline())
num_list = list()

for i in range(n):
    num_list.append(int(sys.stdin.readline()))

for i in num_list:
    binary_num = to_binary_reverse(i)
    index_list = list()

    for j in range(len(binary_num)):
        if binary_num[j] == '1':
            index_list.append(j)

    for j in index_list:
        print(j, end=" ")
    print ()

