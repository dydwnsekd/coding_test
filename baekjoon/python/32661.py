"""
import sys

n = int(sys.stdin.readline())
flight_list = []

for _ in range(n):
    flight_list.append(int(sys.stdin.readline().strip()))

if max(flight_list) // 2 > min(flight_list):
    print(0)
else:
    print(min(flight_list) - max(flight_list) // 2)
"""

import sys

n = int(sys.stdin.readline().strip())
flights = [int(sys.stdin.readline().strip()) for _ in range(n)]

mx = max(flights)
mn = min(flights)

if mx // 2 > mn:
    print(0)
else:
    print(mn - mx // 2)

