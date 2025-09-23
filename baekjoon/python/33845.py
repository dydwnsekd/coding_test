"""
import sys

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

result = ""

for c in t:
    if c not in s:
        result += c

print(result)
"""

import sys

s = set(sys.stdin.readline().strip())
t = sys.stdin.readline().strip()

result = "".join(c for c in t if c not in s)
print(result)

