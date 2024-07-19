import sys

n, x = map(int, sys.stdin.readline().strip().split())
t_list = list(map(int, sys.stdin.readline().strip().split()))
sequence = 0

while True:
    if t_list[sequence % n] < x:
        print((sequence % n) + 1)
        break
    else:
        sequence += 1
        x += 1
