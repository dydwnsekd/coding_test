class binary_conversion:

    def convert_to_binary(self, number):
        binary_num = ""
        while number > 0:
            binary_num = str(number % 2) + binary_num
            number = number // 2

        return binary_num


if __name__ == "__main__":
    converter = binary_conversion()
    print(converter.convert_to_binary(1))
    print(converter.convert_to_binary(2))
    print(converter.convert_to_binary(3))
    print(converter.convert_to_binary(4))
    print(converter.convert_to_binary(5))
    print(converter.convert_to_binary(6))
    print(converter.convert_to_binary(7))
    print(converter.convert_to_binary(8))
    print(converter.convert_to_binary(9))
    print(converter.convert_to_binary(10))
