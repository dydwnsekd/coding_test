import sys


def get_divisor(num):

    divisor_list = []
    if num == 2:
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

