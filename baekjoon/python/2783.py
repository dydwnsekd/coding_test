import sys

kimbob_cost = []

c, g = list(map(int, sys.stdin.readline().split()))
kimbob_cost.append(c/g)

n = int(sys.stdin.readline())

for _ in range(n):
    c, g = list(map(int, sys.stdin.readline().split()))
    kimbob_cost.append(c / g)

print(round(min(kimbob_cost) * 1000, 2))
