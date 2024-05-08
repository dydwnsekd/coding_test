import sys

while True:
    result = 0
    h1, m1, h2, m2 = map(int, sys.stdin.readline().split())
    if h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0:
        break

    time1 = h1 * 60 + m1
    time2 = h2 * 60 + m2

    if time1 <= time2:
        print(time2 - time1)
    else:
        print(1440 - time1 + time2)

