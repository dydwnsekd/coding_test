import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    x, y, a, b = map(int, sys.stdin.readline().split())
    times = 1
    while True:
        if x+a == y-b:
            print(times)
            break
        elif x+a > y-b:
            print(-1)
            break
        else:
            x += a
            y -= b
            times += 1

