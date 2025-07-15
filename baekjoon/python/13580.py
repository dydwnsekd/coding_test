import sys

year_list = list(map(int, sys.stdin.readline().strip().split()))
year_list.sort()

if year_list[0] == year_list[1] or year_list[1] == year_list[2]:
    print("S")
elif year_list[2] == year_list[0] + year_list[1]:
    print("S")
else:
    print("N")

