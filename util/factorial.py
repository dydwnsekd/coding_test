class Factorial:

    @staticmethod
    def get_factorial_num_recursion(num):
        if num == 1:
            return 1
        else:
            return num * Factorial.get_factorial_num(num - 1)

    @staticmethod
    def get_factorial_num_repeat(num):
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result


if __name__ == '__main__':
    print(Factorial.get_factorial_num(10))
    print(Factorial.get_factorial_num(9))
    print(Factorial.get_factorial_num(8))
    print(Factorial.get_factorial_num(7))
    print(Factorial.get_factorial_num(6))
    print(Factorial.get_factorial_num(5))
    print(Factorial.get_factorial_num(4))
    print(Factorial.get_factorial_num(3))
    print(Factorial.get_factorial_num(2))
    print(Factorial.get_factorial_num(1))

