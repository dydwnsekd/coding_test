import sys

n, x = map(int, sys.stdin.readline().strip().split())
score_list = list(map(int, sys.stdin.readline().strip().split()))

total = sum(score_list)
count = 0

while total / n < x:
    total += 100
    n += 1
    count += 1

print(count)
