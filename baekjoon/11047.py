import sys

coin_num, money = list(map(int, sys.stdin.readline().split(" ")))
coin_list = list()
count = 0

for _ in range(coin_num):
    coin_list.append(int(sys.stdin.readline()))

for i in range(coin_num-1, -1, -1):
    count += int(money / coin_list[i])
    money = money % coin_list[i]

print (count)