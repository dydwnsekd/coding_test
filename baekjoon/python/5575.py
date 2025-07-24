"""
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
"""

import sys

for _ in range(3):
    t1_h, t1_m, t1_s, t2_h, t2_m, t2_s = map(int, sys.stdin.readline().split())

    # 시, 분, 초를 모두 초 단위로 변환
    t1_seconds = t1_h * 3600 + t1_m * 60 + t1_s
    t2_seconds = t2_h * 3600 + t2_m * 60 + t2_s

    total_seconds = t2_seconds - t1_seconds

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    print(hours, minutes, seconds)
