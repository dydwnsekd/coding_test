import sys

count = 0

w, n, p = map(int, sys.stdin.readline().split())
punch_list = list(map(int, sys.stdin.readline().split()))

for punch in punch_list:
    if w <= punch <= n:
        count += 1

print(count)
