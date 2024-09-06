import sys


def hexadecimal_to_decimal(hexadecimal_num):
    hexadecimal_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    decimal_num = 0

    hexadecimal_num = hexadecimal_num[::-1]
    for i in range(len(hexadecimal_num)):
        decimal_num += hexadecimal_nums.index(hexadecimal_num[i]) * 16 ** i

    return decimal_num


hexa_num = sys.stdin.readline().strip()

print(hexadecimal_to_decimal(hexa_num))
