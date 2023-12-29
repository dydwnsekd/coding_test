import sys

count = 0
n, m = map(int, sys.stdin.readline().split())

count += n

while n // m >= m:
    count += n // m
    n = n // m

print(count)
