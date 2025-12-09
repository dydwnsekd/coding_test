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
