"""
import sys

n = int(sys.stdin.readline())
result = 0

for _ in range(n):
    visitor, visitor_type, num = sys.stdin.readline().split()
    num = int(num)

    if visitor_type == 'IN':
        result += num
    elif visitor_type == 'OUT':
        result -= num

if result == 0:
    print("NO STRAGGLERS")
else:
    print(result)
"""

import sys

n = int(sys.stdin.readline())
result = 0

for _ in range(n):
    _, visitor_type, num = sys.stdin.readline().split()
    num = int(num)

    if visitor_type == 'IN':
        result += num
    else:
        result -= num

if result:
    print(result)
else:
    print("NO STRAGGLERS")
