import sys

date = sys.stdin.readline()

dt_1 = int(date.split("/")[0])
dt_2 = int(date.split("/")[1])

if 1 <= dt_1 <= 12 and 1 <= dt_2 <= 12:
    print("either")
elif 1 <= dt_1 <= 12 and 12 < dt_2:
    print("US")
elif 12 < dt_1 and 1 <= dt_2 <= 12:
    print("EU")

