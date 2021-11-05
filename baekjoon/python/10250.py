import sys

n = int(sys.stdin.readline())
for i in range(n):
    h, w, n = list(map(int, sys.stdin.readline().split(" ")))
    room_num = str((n // h) + 1)
    floor = str(n % h)
    print(floor + room_num.zfill(2))