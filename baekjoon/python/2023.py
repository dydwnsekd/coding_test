import sys


class eratos:

    @staticmethod
    def is_decimal(num):
        for i in range(2, num):
            if num % i == 0:
                return False

        return True


n = int(sys.stdin.readline())

answer_1 = [2, 3, 5, 7]
answer_2 = []

