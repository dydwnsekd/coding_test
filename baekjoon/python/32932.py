import sys

block = []
start = [0, 0]
n, k = map(int, sys.stdin.readline().strip().split())

for _ in range(n):
    block.append(list(map(int, sys.stdin.readline().strip().split())))

controlls = sys.stdin.readline().strip()

for controll in controlls:
    if controll == 'U':
        if [start[0], start[1] + 1] not in block:
            start = [start[0], start[1] + 1]
    elif controll == 'D':
        if [start[0], start[1] - 1] not in block:
            start = [start[0], start[1] - 1]
    elif controll == 'L':
        if [start[0], start[1] + 1] not in block:
            start = [start[0], start[1] + 1]
    elif controll == 'R':
        if [start[0], start[1] - 1] not in block:
            start = [start[0], start[1] - 1]

print(' '.join(map(str, start)))

