import sys

cases = int(sys.stdin.readline())
quadrant_name = ["Q1", "Q2", "Q3", "Q4", "AXIS"]
q_list = [0, 0, 0, 0, 0]

for _ in range(cases):
    x, y = list(map(int, sys.stdin.readline().split()))
    if x > 0 and y > 0:
        q_list[0] += 1
    elif x < 0 and y > 0:
        q_list[1] += 1
    elif x < 0 and y < 0:
        q_list[2] += 1
    elif x > 0 and y < 0:
        q_list[3] += 1
    else:
        q_list[4] += 1

for i in range(len(quadrant_name)):
    print(f"{quadrant_name[i]}: {q_list[i]}")
