import sys

n = int(sys.stdin.readline())

year_list = list(map(int, sys.stdin.readline().split()))

print(year_list[-1] + year_list[1] - year_list[0])
