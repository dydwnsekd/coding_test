import sys

s = sys.stdin.readline().strip()

if "(" in s:
    station_name = s.split("(")[0]
    sub_station_name = s.split("(")[1][:-1]
    print(station_name)
    print(sub_station_name)
else:
    print(s)
    print("-")
