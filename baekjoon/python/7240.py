"""
import sys

n, s = map(int, sys.stdin.readline().strip().split())
current_speed = 0

for _ in range(n-1):
    current_speed += int(sys.stdin.readline())

    if current_speed > s:
        current_speed -= 1

print(current_speed + int(sys.stdin.readline()))
"""

import sys

n, s = map(int, sys.stdin.readline().split())
changes = [int(sys.stdin.readline()) for _ in range(n)]

current_speed = 0
for i, delta in enumerate(changes):
    current_speed += delta
    if i < n - 1 and current_speed > s:
        current_speed -= 1

print(current_speed)

