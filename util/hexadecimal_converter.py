class hexadecimal_converter:

    def __init__(self):
        self.hexadecimal_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    def decimal_to_hexadecimal(self, decimal_number):
        hexadecimal_num = ""
        
        while decimal_number > 0:
            hexadecimal_num = self.hexadecimal_nums[decimal_number % 16] + hexadecimal_num
            decimal_number = decimal_number // 16

        return hexadecimal_num

    def hexadecimal_to_decimal(self, hexadecimal_num):
        decimal_num = 0

        hexadecimal_num = hexadecimal_num[::-1]
        for i in range(len(hexadecimal_num)):
            decimal_num += self.hexadecimal_nums.index(hexadecimal_num[i]) * 16 ** i
        
        return decimal_num


if __name__ == "__main__":
    converter = hexadecimal_converter()
    for i in range(17):
        hexadecimal_num = converter.decimal_to_hexadecimal(i)
        print(f"========== i = {i} ==========")
        print(f"16진수 : {hexadecimal_num}")
        print(f"10진수 : {converter.hexadecimal_to_decimal(hexadecimal_num)}")
