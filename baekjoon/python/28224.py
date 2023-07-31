import sys

days = int(sys.stdin.readline())
price = 0

for i in range(days):
    price += int(sys.stdin.readline())

print(price)
