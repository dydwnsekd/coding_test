import sys

money = int(sys.stdin.readline())
cal_money = 0
n = int(sys.stdin.readline())

for _ in range(n):
    value, count = list(map(int, sys.stdin.readline().split()))
    cal_money += value * count

if cal_money == money:
    print("Yes")
else:
    print("No")
