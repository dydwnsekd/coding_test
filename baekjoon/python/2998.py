import sys

def binary_to_decimal(binary_num):
    decimal_num = 0

    binary_num = binary_num[::-1]
    for i in range(len(binary_num)):
        decimal_num += int(binary_num[i]) * 2 ** i

    return decimal_num

def decimal_to_octal(decimal_number):
    octal_num = ""
    if decimal_number == 0:
        return "0"
    while decimal_number > 0:
        octal_num = str(decimal_number % 8) + octal_num
        decimal_number = decimal_number // 8

    return octal_num


bin_num = sys.stdin.readline().strip()
print(decimal_to_octal(binary_to_decimal(bin_num)))
