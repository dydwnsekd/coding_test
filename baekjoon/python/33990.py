"""
import sys

n = int(sys.stdin.readline())
k512 = sys.maxsize

for _ in range(n):
    temp = sum(list(map(int, sys.stdin.readline().strip().split())))
    if 512 <= temp < k512:
        k512 = temp

if k512 == sys.maxsize:
    print(-1)
else:
    print(k512)
"""

import sys

n = int(sys.stdin.readline())
k512 = sys.maxsize

for _ in range(n):
    temp = sum(map(int, sys.stdin.readline().split()))
    if temp >= 512:
        k512 = min(k512, temp)

print(-1 if k512 == sys.maxsize else k512)

