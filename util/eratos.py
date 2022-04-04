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

    