import sys

while True:
    n = int(sys.stdin.readline())

    if n == -1:
        break
    else:
        distance = 0
        speed_list = []
        for i in range(n):
            speed_list.append(list(map(int, sys.stdin.readline().strip().split())))
            if i == 0:
                distance += speed_list[i][0] * speed_list[i][1]
            else:
                distance += speed_list[i][0] * (speed_list[i][1] - speed_list[i-1][1])
    print(f"{distance} miles")
