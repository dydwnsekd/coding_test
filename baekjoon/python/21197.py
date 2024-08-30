"""
import sys

result = 0

n = int(sys.stdin.readline())
stop_list = []

for i in range(n):
    stop_list.append(int(sys.stdin.readline()))

if n % 2 == 1:
    print("still running")
else:
    for i in range(1, n, 2):
        result += stop_list[i] - stop_list[i-1]
    print(result)
"""

# ================================================================

import sys

n = int(sys.stdin.readline())

if n % 2 == 1:
    print("still running")
else:
    result = 0
    for i in range(n // 2):
        start_time = int(sys.stdin.readline())
        stop_time = int(sys.stdin.readline())
        result += stop_time - start_time
    print(result)
