"""
import sys

n = int(sys.stdin.readline())
change_count = 0

seat_list = list(map(int, sys.stdin.readline().split()))

i = 1

while True:
    if seat_list[i-1] != 0:
        change_count += 1
        i = seat_list[i-1]
    else:
        break

print(change_count)
"""

import sys

n = int(sys.stdin.readline().strip())
seats = list(map(int, sys.stdin.readline().strip().split()))

count = 0
index = 1

while True:
    next_index = seats[index - 1]
    if next_index == 0:
        break
    count += 1
    index = next_index

print(count)
