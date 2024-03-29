import sys

n = int(sys.stdin.readline())
click_count = [0] * n

durability_list = list(map(int, sys.stdin.readline().split()))

k = int(sys.stdin.readline())
click_log = list(map(int, sys.stdin.readline().split()))

for i in click_log:
    click_count[i-1] += 1

for i in range(n):
    if durability_list[i] < click_count[i]:
        print("yes")
    else:
        print("no")

