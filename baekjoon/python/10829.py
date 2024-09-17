import sys

def decimal_to_binary(decimal_number):
    binary_num = ""
    if decimal_number == 0:
        return "0"
    while decimal_number > 0:
        binary_num = str(decimal_number % 2) + binary_num
        decimal_number = decimal_number // 2

    return binary_num

n = int(sys.stdin.readline())

print(decimal_to_binary(n))
