"""
import sys

m = int(sys.stdin.readline())
park_dict = {}
result_list = []

for _ in range(m):
    t, n = map(int, sys.stdin.readline().split())

    if n not in park_dict:
        park_dict[n] = t
    else:
        result_list.append([n, t - park_dict[n]])
        park_dict.pop(n)

for r in result_list:
    print(*r)
"""

import sys

m = int(sys.stdin.readline().strip())
parking_times = {}

for _ in range(m):
    time, car_id = map(int, sys.stdin.readline().strip().split())

    if car_id not in parking_times:
        parking_times[car_id] = time
    else:
        print(car_id, time - parking_times[car_id])
        del parking_times[car_id]
