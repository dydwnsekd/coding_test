import sys

result = 0

while True:
    betting_money = int(sys.stdin.readline())

    if betting_money == -1:
        break

    result += betting_money

print(result)

