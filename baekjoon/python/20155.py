import sys

n, m = map(int, sys.stdin.readline().strip().split())
mart_list = list(map(int, sys.stdin.readline().strip().split()))

max_count = 0

for i in range(1, m+1):
    if max_count < mart_list.count(i):
        max_count = mart_list.count(i)

print(max_count)


