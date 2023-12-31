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

    def duodecimal_to_decimal(self, duodecimal_num):
        decimal_num = 0

        duodecimal_num = duodecimal_num[::-1]
        for i in range(len(duodecimal_num)):
            decimal_num += self.duodecimal_nums.index(duodecimal_num[i]) * 12 ** i

        return decimal_num


if __name__ == "__main__":
    converter = duodecimal_converter()
    for i in range(17):
        duodecimal_num = converter.decimal_to_duodecimal(i)
        print(f"========== i = {i} ==========")
        print(f"12진수 : {duodecimal_num}")
        print(f"10진수 : {converter.duodecimal_to_decimal(duodecimal_num)}")
