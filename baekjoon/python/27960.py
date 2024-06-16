import sys


def decimal_to_binary(decimal_number):
    binary_num = ""
    if decimal_number == 0:
        return "0"
    while decimal_number > 0:
        binary_num = str(decimal_number % 2) + binary_num
        decimal_number = decimal_number // 2

    return binary_num


c = 0
target_score = 512
a, b = map(int, (sys.stdin.readline().strip().split()))

bin_a = decimal_to_binary(a).zfill(10)
bin_b = decimal_to_binary(b).zfill(10)


for i in range(10):
    if bin_a[i] != bin_b[i]:
        c += target_score

    target_score //= 2

print(c)

