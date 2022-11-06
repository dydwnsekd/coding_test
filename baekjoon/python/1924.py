import sys

month_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
month, day = list(map(int, sys.stdin.readline().split()))

result = 0

for i in range(month):
    result += month_day[i]

result += day
result %= 7

if result == 1:
    print("MON")
elif result == 2:
    print("TUE")
elif result == 3:
    print("WED")
elif result == 4:
    print("THU")
elif result == 5:
    print("FRI")
elif result == 6:
    print("SAT")
elif result == 0:
    print("SUN")
