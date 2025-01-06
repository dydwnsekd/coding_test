import sys

pow_gap = [1]
for i in range(2, 1000):
    pow_gap.append(i ** 2 - pow_gap[-1])

n = int(sys.stdin.readline())

print(pow_gap.count(n))
