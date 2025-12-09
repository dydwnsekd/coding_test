"""
import sys

index = 1
result = 0

n = int(sys.stdin.readline())
box_command = sys.stdin.readline().strip()

for i in box_command:
    if i == "R":
        if index >= 2:
            result += 1
            index = 3
        else:
            index += 1
    elif i == "L":
        if index <= 2:
            index = 1
        else:
            index -= 1

print(result)
"""

import sys

index = 1
result = 0

n = int(sys.stdin.readline().strip())
commands = sys.stdin.readline().strip()

for cmd in commands:
    if cmd == 'R':
        if index == 1:
            index = 2
        else:
            result += 1
            index = 3
    else:  # cmd == 'L'
        if index == 3:
            index = 2
        else:
            index = 1

print(result)

