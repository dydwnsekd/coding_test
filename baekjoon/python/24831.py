import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    x, y, a, b = map(int, sys.stdin.readline().split())
    times = 1

    distance = y - x
    jump_distance = a + b

    if distance % jump_distance == 0:
        print(distance // jump_distance)
    else:
        print(-1)
