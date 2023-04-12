import sys


def divisor_list(num):
    divisor_list = []

    for i in range(1, num):
        if num % i == 0:
            divisor_list.append(i)

    return divisor_list


while True:
    num = int(sys.stdin.readline())

    if num == -1:
        break

    if sum(divisor_list(num)) == num:
        print(f"{num} = ", end="")
        print(" + ".join(map(str, divisor_list(num))))
    else:
        print(f"{num} is NOT perfect.")

