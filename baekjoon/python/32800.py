import sys

current_passenger = 0
max_passenger = -1

n = int(sys.stdin.readline())

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    current_passenger -= a
    current_passenger += b

    max_passenger = max(current_passenger, max_passenger)

print(max_passenger)


