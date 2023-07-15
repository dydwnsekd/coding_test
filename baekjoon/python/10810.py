import sys

n, m = map(int, sys.stdin.readline().split())
basket = [0] * n

for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().split())

    for basket_num in range(i-1, j):
        basket[basket_num] = k

print(*basket)
