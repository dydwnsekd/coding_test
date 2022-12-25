import sys

k, w, m = list(map(int, sys.stdin.readline().split()))
count = 0

while True:
    if k >= w:
        print(count)
        break
    else:
        k += m
        count += 1
