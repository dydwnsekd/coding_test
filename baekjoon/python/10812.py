import sys

n, m = list(map(int, sys.stdin.readline().split()))
basket = [i for i in range(1, n+1)]

for i in range(m):
    start, end, mid = list(map(int, sys.stdin.readline().split()))
    basket = basket[:start-1] + basket[mid-1:end] + basket[start-1:mid-1] + basket[end:]

for i in basket:
    print(i, end=" ")
