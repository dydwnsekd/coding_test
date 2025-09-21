import sys

n, s = map(int, sys.stdin.readline().strip().split())
current_speed = 0

for _ in range(n-1):
    current_speed += int(sys.stdin.readline())

    if current_speed > s:
        current_speed -= 1

print(current_speed + int(sys.stdin.readline()))
