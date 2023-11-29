import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    x, y, z = list(map(int, sys.stdin.readline().split()))
    need_seconds = 0

    while True:
        x += z * need_seconds
        if x >= y:
            print(need_seconds)
            break
        need_seconds += 1

