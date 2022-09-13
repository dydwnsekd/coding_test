import sys

k, n, m = list(map(int, sys.stdin.readline().split()))

need_money = k * n
if need_money > m:
    print(need_money-m)
else:
    print(0)
