"""
import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

while n > 0:
    n -= 1
    result = ""
    num_count = 1

    for i in range(len(s)):
        if i + 1 == len(s):
            result += f"{num_count}{s[i]}"
        elif s[i] == s[i+1]:
            num_count += 1
        else:
            result += f"{num_count}{s[i]}"
            num_count = 1

    s = result

print(s)
"""

import sys
from itertools import groupby

n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()

for _ in range(n):
    s = "".join(f"{len(list(g))}{k}" for k, g in groupby(s))

print(s)
