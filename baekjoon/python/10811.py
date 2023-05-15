import sys

n, m = map(int, sys.stdin.readline().split())
basket = []
for i in range(1, n+1):
    basket.append(i)

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())

    temp = basket[i-1:j]
    temp.reverse()

    basket[i-1:j] = temp

print(*basket)
