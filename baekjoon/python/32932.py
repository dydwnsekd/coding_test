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

