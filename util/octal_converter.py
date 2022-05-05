class binary_converter:

    def decimal_to_octal(self, decimal_number):
        binary_num = ""
        while decimal_number > 0:
            binary_num = str(decimal_number % 8) + binary_num
            decimal_number = decimal_number // 8

        return binary_num

    def octal_to_decimal(self, binary_num):
        decimal_num = 0

        binary_num = binary_num[::-1]
        for i in range(len(binary_num)):
            decimal_num += int(binary_num[i]) * 8 ** i
        
        return decimal_num


if __name__ == "__main__":
    converter = binary_converter()
    print(converter.decimal_to_octal(1))
    print(converter.decimal_to_octal(2))
    print(converter.decimal_to_octal(3))
    print(converter.decimal_to_octal(4))
    print(converter.decimal_to_octal(5))
    print(converter.decimal_to_octal(6))
    print(converter.decimal_to_octal(7))
    print(converter.decimal_to_octal(8))
    print(converter.decimal_to_octal(9))
    print(converter.decimal_to_octal(10))

    print(converter.octal_to_decimal("1"))
    print(converter.octal_to_decimal("2"))
    print(converter.octal_to_decimal("3"))
    print(converter.octal_to_decimal("4"))
    print(converter.octal_to_decimal("5"))
    print(converter.octal_to_decimal("6"))
    print(converter.octal_to_decimal("7"))
    print(converter.octal_to_decimal("10"))
    print(converter.octal_to_decimal("11"))
    print(converter.octal_to_decimal("12"))
