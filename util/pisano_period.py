class PisanoPeriod:

    def pisano_period(self, m):
        previous, current = 0, 1
        for i in range(0, m * m):
            previous, current = current, (previous + current) % m

            if previous == 0 and current == 1:
                return i + 1

    def pisano_period_list(self, m):
        previous, current = 0, 1
        pisano_list = [0]
        for i in range(0, m * m):
            previous, current = current, (previous + current) % m

            if previous == 0 and current == 1:
                return pisano_list
            pisano_list.append(previous)


if __name__ == '__main__':
    pisano_period = PisanoPeriod()
    print(pisano_period.pisano_period(4))
    print(pisano_period.pisano_period_list(4))
    print(pisano_period.pisano_period(5))
    print(pisano_period.pisano_period_list(5))
    print(pisano_period.pisano_period(11))
    print(pisano_period.pisano_period_list(11))
    # print(pisano_period.pisano_period(123456))
    # print(pisano_period.pisano_period_list(123456))
    # print(pisano_period.pisano_period(987654))
    # print(pisano_period.pisano_period_list(987654))
