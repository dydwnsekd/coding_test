'''
import sys

def prime_list(num):
    prime_flag = [True] * num

    m = int(num ** 0.5)
    for i in range(2, m + 1):
        if prime_flag[i]:
            for j in range(i * i, num, i):
                prime_flag[j] = False

    return [i for i in range(2, num) if prime_flag[i]]

prime_list = prime_list(10010)

n = int(sys.stdin.readline())

for _ in range(n):
    v = int(sys.stdin.readline())

    print(f"Input value: {v}")

    if v in prime_list:
        print("Would you believe it; it is a prime!\n")
    else:
        min_distance = 10000
        for i in prime_list:
            if abs(i-v) < min_distance:
                min_distance = abs(i-v)

        print(f"Missed it by that much ({min_distance})!\n")
'''

import sys

def generate_primes(limit: int):
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False

    return [i for i in range(2, limit) if is_prime[i]]


primes = generate_primes(10010)
prime_set = set(primes)

n = int(sys.stdin.readline().strip())

for _ in range(n):
    v = int(sys.stdin.readline().strip())
    print(f"Input value: {v}")

    if v in prime_set:
        print("Would you believe it; it is a prime!\n")
    else:
        min_distance = 10000
        for p in primes:
            diff = abs(p - v)
            if diff >= min_distance:
                break
            min_distance = diff

        print(f"Missed it by that much ({min_distance})!\n")

