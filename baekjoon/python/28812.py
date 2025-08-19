import sys

price_list = []
n, c = map(int, sys.stdin.readline().strip().split())

for _ in range(n):
    p, d, v = map(int, sys.stdin.readline().strip().split())
    price_list.append((p+d+(c*v)))

print(min(price_list))


