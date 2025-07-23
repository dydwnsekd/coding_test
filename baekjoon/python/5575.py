import sys
from datetime import datetime

for _ in range(3):
    t1_h, t1_m, t1_s, t2_h, t2_m, t2_s = map(int, sys.stdin.readline().strip().split())

    t1 = datetime(year=2000, month=1, day=1, hour=t1_h, minute=t1_m, second=t1_s)
    t2 = datetime(year=2000, month=1, day=1, hour=t2_h, minute=t2_m, second=t2_s)

    t_diff = t2 - t1
    total_seconds = int(t_diff.total_seconds())

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    print(hours, minutes, seconds)

