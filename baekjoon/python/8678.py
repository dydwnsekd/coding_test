import sys


def get_divisor(num):

    divisor_list = []
    for i in range(1, num//2):
        if num % i == 0:
            if i not in divisor_list:
                divisor_list.append(i)
                divisor_list.append(num // i)

    divisor_list.sort()
    return divisor_list


n = int(sys.stdin.readline())

for i in range(n):
    flag = True
    a, b = list(map(int, sys.stdin.readline().split()))
    a_divisor = get_divisor(a)
    b_divisor = get_divisor(b)

    for i in a_divisor:
        if i not in b_divisor:
            flag = False

    if flag:
        print("TAK")
    else:
        print("NIE")

