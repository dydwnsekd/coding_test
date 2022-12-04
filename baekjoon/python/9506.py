import sys


def prime_list(num):
    prime_flag = [True] * num

    m = int(num ** 0.5)
    for i in range(2, m + 1):
        if prime_flag[i]:
            for j in range(i * i, num, i):
                prime_flag[j] = False

    return [i for i in range(2, num) if prime_flag[i]]


while True:
    n = int(sys.stdin.readline())

    print("n :::", n)
    print("sum :::")
    for i in prime_list(n)[:-1]:
        print(i, end=" ")

    if n == -1:
        break
    else:
        if n == sum(prime_list(n)):
            print(f"{n} = {prime_list}".format(n=n, prime_list=" + ".join(prime_list(n))))
        else:
            print("{n} is NOT perfect.".format(n=n))
