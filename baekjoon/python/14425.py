import sys
origin_list = []
count = 0

n, m = list(map(int, sys.stdin.readline().split()))

for _ in range(n):
    origin_list.append(input())

for _ in range(m):
    if input() in origin_list:
        count += 1

print(count)
