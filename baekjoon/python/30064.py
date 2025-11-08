import sys

n = int(sys.stdin.readline())
change_count = 0

seat_list = list(map(int, sys.stdin.readline().split()))

i = 1

while True:
    if seat_list[i-1] != 0:
        change_count += 1
        i = seat_list[i-1]
    else:
        break

print(change_count)
