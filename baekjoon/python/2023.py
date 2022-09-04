import sys

class eratos:

    @staticmethod
    def prime_list(num):
        prime_flag = [True] * num

        m = int(num ** 0.5)
        for i in range(2, m + 1):
            if prime_flag[i]:
                for j in range(i * i, num, i):
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


n = sys.stdin.readline()
int_n = int(n)

sosu_list = eratos.prime_list(10 ** int_n)
filtered_sosu = []

for sosu in sosu_list:
    if len(str(sosu)) == int_n:
        filtered_sosu.append(sosu)

print(filtered_sosu)
