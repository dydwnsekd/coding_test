import sys

d = int(sys.stdin.readline())

while True:
    yobi = int(sys.stdin.readline())
    if d > yobi:
        d += yobi
    else:
        break

print(d)
