import sys

count = 0

n, h = map(int, sys.stdin.readline().strip().split())
h_list = list(map(int, sys.stdin.readline().strip().split()))

for i in h_list:
    if i <= h:
        count += 1

print(count)
