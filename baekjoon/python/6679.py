import sys

class hexadecimal_converter:

    def __init__(self):
        self.hexadecimal_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    def decimal_to_hexadecimal(self, decimal_number):
        hexadecimal_num = ""
        if decimal_number == 0:
            return "0"
        while decimal_number > 0:
            hexadecimal_num = self.hexadecimal_nums[decimal_number % 16] + hexadecimal_num
            decimal_number = decimal_number // 16

        return hexadecimal_num

    def digit_sum(self, decimal_num):
        digit_sum = 0
        hex_num = self.decimal_to_hexadecimal(decimal_num)

        for i in hex_num:
            digit_sum += self.hexadecimal_nums.index(i)

        return digit_sum

class duodecimal_converter:

    def __init__(self):
        self.duodecimal_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B']

    def decimal_to_duodecimal(self, decimal_number):
        duodecimal_num = ""
        if decimal_number == 0:
            return "0"
        while decimal_number > 0:
            duodecimal_num = self.duodecimal_nums[decimal_number % 12] + duodecimal_num
            decimal_number = decimal_number // 12

        return duodecimal_num

    def digit_sum(self, decimal_num):
        digit_sum = 0
        hex_num = self.decimal_to_duodecimal(decimal_num)

        for i in hex_num:
            digit_sum += self.duodecimal_nums.index(i)

        return digit_sum

def digit_sum(num):
    digit_sum = 0
    for i in str(num):
        digit_sum += int(i)

    return digit_sum

hex_converter = hexadecimal_converter()
duo_converter = duodecimal_converter()

for i in range(1000, 10000):
    if digit_sum(i) == hex_converter.digit_sum(i) == duo_converter.digit_sum(i):
        print(i)

