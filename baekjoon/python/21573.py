import sys

troom, tcond = map(int, sys.stdin.readline().strip().split())
mode = sys.stdin.readline().strip()

if mode == "freeze":
    if troom < tcond:
        print(troom)
    else:
        print(tcond)
elif mode == "heat":
    if troom > tcond:
        print(troom)
    else:
        print(tcond)
elif mode == "auto":
    print(tcond)
elif mode == "fan":
    print(troom)


