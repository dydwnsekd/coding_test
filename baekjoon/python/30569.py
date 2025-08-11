import sys

p1h, p1d, p1t = map(int, sys.stdin.readline().strip().split())
p2h, p2d, p2t = map(int, sys.stdin.readline().strip().split())

p1h -= p2d
p2h -= p1d

p1k = 1
p2k = 1

if p1h < 0 and p2h < 0:
    print("draw")
elif p1h > 0 and p2h < 0:
    print("player one")
elif p1h < 0 and p2h > 0:
    print("player two")
else:
    while True:
        if p1h <= p2d * p2k:
            p2k = p2k * p2t
            break
        else:
            p2k += 1

    while True:
        if p2h <= p1d * p1k:
            p1k = p1k * p1t
            break
        else:
            p1k += 1

    if p1k > p2k:
        print("player two")
    elif p1k < p2k:
        print("player one")
    else:
        print("draw")
