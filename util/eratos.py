class eratos:

    @staticmethod
    def prime_list(num):
        prime_flag = [True] * num
        
        m = int(num ** 0.5)
        for i in range(2, m+1):
            if prime_flag[i]:
                for j in range(i*i, num, i):
                    prime_flag[j] = False

        return [i for i in range(2, num) if prime_flag[i]]

    @staticmethod
    def is_decimal(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        
        return True

    @staticmethod
    def prime_count(num):
        return len(eratos.prime_list(num))


if __name__ == "__main__":
    print(eratos.prime_list(100))
    print(eratos.is_decimal(10))
    print(eratos.prime_count(100))