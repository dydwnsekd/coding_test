import sys

t1 = 300
t2 = 60
t3 = 10

t = int(sys.stdin.readline())

if t % t3 == 0:
    c1 = t // t1
    t = t % t1
    c2 = t // t2
    t = t % t2
    c3 = t // t3
    t = t % t3

    print(f"{c1} {c2} {c3}")
else:
    print(-1)
