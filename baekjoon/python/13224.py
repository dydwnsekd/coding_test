import sys

ball_position = 1
s = list(sys.stdin.readline())

for i in s:
    if i == "A":
        if ball_position == 1:
            ball_position = 2
        elif ball_position == 2:
            ball_position = 1
    elif i == "B":
        if ball_position == 2:
            ball_position = 3
        elif ball_position == 3:
            ball_position = 2
    elif i == "C":
        if ball_position == 1:
            ball_position = 3
        elif ball_position == 3:
            ball_position = 1

print(ball_position)
