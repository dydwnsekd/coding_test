class binary_converter:

    def decimal_to_binary(self, decimal_number):
        binary_num = ""
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
    print(converter.decimal_to_binary(1))
    print(converter.decimal_to_binary(2))
    print(converter.decimal_to_binary(3))
    print(converter.decimal_to_binary(4))
    print(converter.decimal_to_binary(5))
    print(converter.decimal_to_binary(6))
    print(converter.decimal_to_binary(7))
    print(converter.decimal_to_binary(8))
    print(converter.decimal_to_binary(9))
    print(converter.decimal_to_binary(10))

    print(converter.binary_to_decimal("1"))
    print(converter.binary_to_decimal("10"))
    print(converter.binary_to_decimal("11"))
    print(converter.binary_to_decimal("100"))
    print(converter.binary_to_decimal("101"))
    print(converter.binary_to_decimal("110"))
    print(converter.binary_to_decimal("111"))
    print(converter.binary_to_decimal("1000"))
    print(converter.binary_to_decimal("1001"))
    print(converter.binary_to_decimal("1010"))
