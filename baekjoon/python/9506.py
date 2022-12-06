import sys


def prime_list(num):
    prime_flag = [True] * num

    m = int(num ** 0.5)
    for i in range(2, m + 1):
        if prime_flag[i]:
            for j in range(i * i, num, i):
                prime_flag[j] = False

    return [i for i in range(1, num) if prime_flag[i]]


while True:
    n = int(sys.stdin.readline())

    if n == -1:
        break
    else:
        if n == sum(prime_list(n)[:-1]):
            prime_str = [str(i) for i in prime_list(n)]
            print("{n} = {prime_list}".format(n=n, prime_list=" + ".join(prime_str)))
        else:
            prime_str = [str(i) for i in prime_list(n)]
            print(f"{n} is NOT perfect.")
