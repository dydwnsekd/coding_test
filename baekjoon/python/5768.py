import sys

def get_divisor_counter(num):

    divisor_list = []
    if num == 2:
        return 2
    elif num == 3:
        return 2

    for i in range(1, num//2 + 1):
        if num % i == 0:
            divisor_list.append(i)
            divisor_list.append(num // i)

    divisor_list = list(set(divisor_list))
    divisor_list.sort()
    return len(divisor_list)


while True:
    m, n = map(int, sys.stdin.readline().strip().split())

    if m == 0 and n == 0:
        break

    max_division_count = 0
    max_num = m

    for i in range(m, n):
        if i >= max_num and get_divisor_counter(i) >= max_division_count:
            max_division_count = get_divisor_counter(i)
            max_num = i

    print(max_num, max_division_count)


