import sys


def change_money(money):
    result = []
    money_unit = [25, 10, 5, 1]

    for i in money_unit:
        result.append(money // i)
        money %= i

    return result


n = int(sys.stdin.readline())

for _ in range(n):
    money = int(sys.stdin.readline())
    result = change_money(money)
    for i in result:
        print(i, end=" ")
    print()
