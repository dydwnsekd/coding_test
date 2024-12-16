class PisanoPeriod:

    def pisano_period(self, m):
        previous, current = 0, 1
        for i in range(0, m * m):
            # 피보나치 수열의 나머지 계산
            previous, current = current, (previous + current) % m

            # 주기가 시작되는 조건
            if previous == 0 and current == 1:
                return i + 1


if __name__ == '__main__':
    pisano_period = PisanoPeriod()
    print(pisano_period.pisano_period(4))
    print(pisano_period.pisano_period(5))
    print(pisano_period.pisano_period(11))
    print(pisano_period.pisano_period(123456))
    print(pisano_period.pisano_period(987654))
