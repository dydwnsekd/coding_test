import sys

minkuk = list(map(int, sys.stdin.readline().split(" ")))
manse = list(map(int, sys.stdin.readline().split(" ")))

min_sum = sum(minkuk)
man_sum = sum(manse)

if min_sum > man_sum:
    print(min_sum)
else:
    print (man_sum)
