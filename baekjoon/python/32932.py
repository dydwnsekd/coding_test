"""
import sys

block = []
coordinate = [0, 0]
n, k = map(int, sys.stdin.readline().strip().split())

for _ in range(n):
    block.append(list(map(int, sys.stdin.readline().strip().split())))

controlls = sys.stdin.readline().strip()

for controll in controlls:
    if controll == 'U':
        if [coordinate[0], coordinate[1] + 1] not in block:
            coordinate = [coordinate[0], coordinate[1] + 1]
    elif controll == 'D':
        if [coordinate[0], coordinate[1] - 1] not in block:
            coordinate = [coordinate[0], coordinate[1] - 1]
    elif controll == 'L':
        if [coordinate[0] - 1, coordinate[1]] not in block:
            coordinate = [coordinate[0] - 1, coordinate[1]]
    elif controll == 'R':
        if [coordinate[0] + 1, coordinate[1]] not in block:
            coordinate = [coordinate[0] + 1, coordinate[1]]

print(' '.join(map(str, coordinate)))
"""

import sys

n, k = map(int, sys.stdin.readline().strip().split())

blocked = {tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)}

controls = sys.stdin.readline().strip()

x, y = 0, 0
DIR = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

for c in controls:
    dx, dy = DIR[c]
    nx, ny = x + dx, y + dy
    if (nx, ny) not in blocked:
        x, y = nx, ny

print(x, y)
