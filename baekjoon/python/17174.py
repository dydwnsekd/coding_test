import sys

count = 0
n, m = map(int, sys.stdin.readline().split())

count += n
count += n // m

if n // m > 1:
    count += 1

print(count)
