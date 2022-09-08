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

    return answer


n = int(sys.stdin.readline())
num_len = 1
sosu_list = ["2", "3", "5", "7"]

while num_len != n:
    sosu_list = add_sosu_num(sosu_list)
    num_len += 1

for i in sosu_list:
    print(i)
