import sys

n = int(sys.stdin.readline())
count = 0

car_list = list(map(int, sys.stdin.readline().split(" ")))

for i in car_list:
    if i == n:
        count += 1

print (count)