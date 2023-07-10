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

    def ones_complement(self, decimal_number: int, length: int):
        bin_number = bin(decimal_number)[2:].zfill(length)
        return_number = ''.join('1' if b == '0' else '0' for b in bin_number)

        return return_number

    def twos_complement(self, decimal_number, length):
        bin_number = bin(decimal_number)[2:].zfill(length)
        temp_number = ''.join('1' if b == '0' else '0' for b in bin_number)
        return_number = bin(int("0b" + temp_number, 2) + 1)[2:].zfill(length)

        return return_number


if __name__ == "__main__":
    converter = binary_converter()
    for i in range(17):
        binary_num = converter.decimal_to_binary(i)
        print(f"========== i = {i} ==========")
        print(f"2진수 : {binary_num}")
        print(f"10진수 : {converter.binary_to_decimal(binary_num)}")
        print(f"1의 보수 : {converter.ones_complement(i, 8)}")
        print(f"2의 보수 : {converter.twos_complement(i, 8)}")
