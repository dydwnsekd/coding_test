import sys

while True:
    l, w, a = list(map(int, sys.stdin.readline().split()))
    if l == 0 and w == 0 and a == 0:
        break
    else:
        if l == 0:
            l = a // w
        elif w == 0:
            w = a // l
        else:
            a = l * w
    print(l, w, a)

