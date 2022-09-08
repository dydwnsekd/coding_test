import sys


def is_decimal(num):
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def add_sosu_num(arr: list):
    sosu_list = ["1", "3", "5", "7", "9"]
    answer = []
    for i in arr:
        for j in sosu_list:
            if is_decimal(int(i+j)):
                answer.append(i+j)


n = int(sys.stdin.readline())
init_list = ["2", "3", "5", "7"]

