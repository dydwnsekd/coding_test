import sys

m = int(sys.stdin.readline())

position = 1

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    if x == position:
        position = y
    elif y == position:
        position = x

print(position)

