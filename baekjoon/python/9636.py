import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    x = 0
    y = 0
    random_count = 0

    s = sys.stdin.readline().strip()

    for i in s:
        if i == "U":
            y += 1
        elif i == "D":
            y -= 1
        elif i == "R":
            x += 1
        elif i == "L":
            x -= 1
        else:
            random_count += 1

    print(f"{x-random_count} {y-random_count} {x+random_count} {y+random_count}")
