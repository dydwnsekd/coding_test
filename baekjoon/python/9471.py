import sys

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 2:
        factors.append(n)

    return factors


n = int(sys.stdin.readline())

for i in range(n):
    case_num, m = map(int, sys.stdin.readline().strip().split())
    m_factors = prime_factors(m)

    if all(factor == 2 for factor in m_factors):
        print(case_num, 3 * (2 ** (len(m_factors) - 1)))
    elif all(factor == 5 for factor in m_factors):
        print(case_num, 4 * (5 ** len(m_factors)))
    elif m_factors.count(2) == 1 and m_factors.count(5) == len(m_factors) - 1:
        print(case_num, 6 * len(m_factors))


