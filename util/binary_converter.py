class binary_converter:

    def decimal_to_binary(self, decimal_number):
        binary_num = ""
        if decimal_number == 0:
            return "0"
        while decimal_number > 0:
            binary_num = str(decimal_number % 2) + binary_num
            decimal_number = decimal_number // 2

        return binary_num

    def binary_to_decimal(self, binary_num):
        decimal_num = 0

        binary_num = binary_num[::-1]
        for i in range(len(binary_num)):
            decimal_num += int(binary_num[i]) * 2 ** i
        
        return decimal_num


if __name__ == "__main__":
    converter = binary_converter()
    for i in range(17):
        binary_num = converter.decimal_to_binary(i)
        print(f"========== i = {i} ==========")
        print(f"2진수 : {binary_num}")
        print(f"10진수 : {converter.binary_to_decimal(binary_num)}")
