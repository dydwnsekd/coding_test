import sys

x, y = map(int, sys.stdin.readline().strip().split())
n = int(sys.stdin.readline())

for _ in range(n):
    temp_x, temp_y = map(int, sys.stdin.readline().strip().split())
    if temp_x == x or temp_y == y:
        print(0)
    else:
        print(1)
