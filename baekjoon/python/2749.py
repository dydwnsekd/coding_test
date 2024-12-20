import sys


class PisanoPeriod:

    @staticmethod
    def pisano_period(m):
        previous, current = 0, 1
        for i in range(0, m * m):
            previous, current = current, (previous + current) % m

            if previous == 0 and current == 1:
                return i + 1

    @staticmethod
    def pisano_period_list(m):
        previous, current = 0, 1
        pisano_list = [0]
        for i in range(0, m * m):
            previous, current = current, (previous + current) % m

            if previous == 0 and current == 1:
                return pisano_list
            pisano_list.append(previous)


num = int(sys.stdin.readline())

pisano_list = PisanoPeriod.pisano_period_list(1000000)
print(pisano_list[num] % PisanoPeriod.pisano_period(1000000))