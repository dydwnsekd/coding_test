import sys

cases = int(sys.stdin.readline())

for i in range(1, cases+1):
    h, m = map(int, sys.stdin.readline().split())

    if m < 45:
        if h == 0:
            h = 23
        else:
            h -= 1
        m = 60 - (45 - m)
    else:
        m -= 45

    print(f"Case #{i}: {h} {m}")

