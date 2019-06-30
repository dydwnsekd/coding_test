import sys

money = 1000
count = 0

get_money = int(sys.stdin.readline())

money_list = [500, 100, 50, 10, 5, 1]
money -= get_money

for i in money_list:
    count += int(money / i)
    money = money % i

print (count)