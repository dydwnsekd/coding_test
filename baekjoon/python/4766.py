import sys

prev_temp = 0

while True:
    temp = float(sys.stdin.readline())
    if temp == 999:
        break
    if prev_temp != 0:
        print(temp-prev_temp)
    prev_temp = temp