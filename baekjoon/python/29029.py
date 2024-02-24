import sys

max_count = 0
directions = ["N", "S", "W", "E"]
n = int(sys.stdin.readline())
direction_list = list(sys.stdin.readline().strip())

for d in directions:
    if max_count < direction_list.count(d):
        max_count = direction_list.count(d)

print(n-max_count)
