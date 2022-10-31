import sys

wide_receiver = [4.5, 150, 200]
lineman = [6.0, 300, 500]
quarterback = [5.0, 200, 300]

while True:
    flag = True

    speed, weight, strength = list(map(float, sys.stdin.readline().split()))
    if speed == 0 and weight == 0 and strength == 0:
        break
    else:
        if speed <= wide_receiver[0] and weight >= wide_receiver[1] and strength >= wide_receiver[2]:
            flag = False
            print("Wide Receiver ", end="")
        if speed <= lineman[0] and weight >= lineman[1] and strength >= lineman[2]:
            flag = False
            print("Lineman ", end="")
        if speed <= quarterback[0] and weight >= quarterback[1] and strength >= quarterback[2]:
            flag = False
            print("Quarterback ", end="")
        if flag:
            print("No positions ", end="")
        print()

