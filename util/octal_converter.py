class octal_converter:

    def decimal_to_octal(self, decimal_number):
        octal_num = ""
        if decimal_number == 0:
            return "0"
        while decimal_number > 0:
            octal_num = str(decimal_number % 8) + octal_num
            decimal_number = decimal_number // 8

        return octal_num

    def octal_to_decimal(self, octal_num):
        decimal_num = 0

        octal_num = octal_num[::-1]
        for i in range(len(octal_num)):
            decimal_num += int(octal_num[i]) * 8 ** i
        
        return decimal_num


if __name__ == "__main__":
    converter = octal_converter()
    for i in range(17):
        octal_num = converter.decimal_to_octal(i)
        print(f"========== i = {i} ==========")
        print(f"8진수 : {octal_num}")
        print(f"10진수 : {converter.octal_to_decimal(octal_num)}")
