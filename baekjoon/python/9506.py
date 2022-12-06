import sys


def divisor_list(num):
    divisor_list = []

    for i in range(1, num):
        if num % i == 0:
            divisor_list.append(i)

    return divisor_list


while True:
    n = int(sys.stdin.readline())

    if n == -1:
        break
    else:
        divisor_str = [str(i) for i in divisor_list(n)]
        if n == sum(divisor_list(n)[:-1]):
            print("{n} = {prime_list}".format(n=n, prime_list=" + ".join(divisor_str)))
        else:
            print("test => {n} = {prime_list}".format(n=n, prime_list=" + ".join(divisor_str)))
            print(f"{n} is NOT perfect.")
