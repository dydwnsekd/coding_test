import sys

food_price = []
result = 0

n = int(sys.stdin.readline())

for i in range(n):
    food_price.append(int(sys.stdin.readline()))

m = int(sys.stdin.readline())

for i in range(m):
    result += food_price[int(sys.stdin.readline())-1]

print(result)
