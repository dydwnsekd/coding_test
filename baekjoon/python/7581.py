import sys

while True:
    values = list(map(int, sys.stdin.readline().split()))

    if sum(values) == 0:
        break

    if values[3] == 0:
        print(values[0] * values[1] * values[2])
    else:
        temp = 1
        for i in values[:3]:
            if i != 0:
                temp *= i

        print(values[3] // temp)
