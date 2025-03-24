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

t = int(sys.stdin.readline())

for _ in range(t):
    flag = True
    n = int(sys.stdin.readline())

    divisor_list = get_divisor(n)
    divisor_sum = sum(divisor_list[:-1])

    for i in divisor_list[1:-1]:
        i_divisor_list = get_divisor(i)
        i_divisor_sum = sum(i_divisor_list[:-1])

        if i < i_divisor_sum:
            flag = False
            break

    if n < divisor_sum and flag:
        print("Good Bye")
    else:
        print("BOJ 2022")
