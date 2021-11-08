import sys

n = int(sys.stdin.readline())
for i in range(n):
    h, w, n = list(map(int, sys.stdin.readline().split(" ")))

    if n <= h:
        floor = str(n)
        room_num = '1'
    elif h == 1:
        floor = '1'
        room_num = str(n)
    elif n % h == 0:
        floor = str(h)
        room_num = str(n // h)
    else:
        room_num = str((n // h) + 1)
        floor = str(n % h)
    print(floor + room_num.zfill(2))