class PrimeFactors:
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


if __name__ == '__main__':
    pf = PrimeFactors()

    print(pf.prime_factors(4))
    print(pf.prime_factors(30))
    print(pf.prime_factors(50))
    print(pf.prime_factors(125))
    print(pf.prime_factors(1024))

