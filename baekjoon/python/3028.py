import sys

ball_index = 1
change_list = sys.stdin.readline().strip()

for i in change_list:
    if i == "A":
        if ball_index == 1:
            ball_index = 2
        elif ball_index == 2:
            ball_index = 1

    if i == "B":
        if ball_index == 2:
            ball_index = 3
        elif ball_index == 3:
            ball_index = 2

    if i == "C":
        if ball_index == 1:
            ball_index = 3
        elif ball_index == 3:
            ball_index = 1

print(ball_index)

