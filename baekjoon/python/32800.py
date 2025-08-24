import sys

current_passenger = 0
max_passenger = -1

n = int(sys.stdin.readline())

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    current_passenger -= a
    current_passenger += b

    if current_passenger > max_passenger:
        max_passenger = current_passenger

print(max_passenger)


