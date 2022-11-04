import sys

prev_temp = -15

while True:
    temp = float(sys.stdin.readline())
    if temp == 999:
        break
    if prev_temp >= -10:
        print("{:.2f}".format(temp-prev_temp))
    prev_temp = temp
