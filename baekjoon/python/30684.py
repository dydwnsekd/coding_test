"""
import sys

n = int(sys.stdin.readline())
name_list = []

for _ in range(n):
    name = sys.stdin.readline().strip()
    if len(name) == 3:
        name_list.append(name)

print(sorted(name_list)[0])
"""

import sys

n = int(sys.stdin.readline())
names = [sys.stdin.readline().strip() for _ in range(n)]

valid_names = [name for name in names if len(name) == 3]
print(min(valid_names))
