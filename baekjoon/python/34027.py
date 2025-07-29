"""
import sys
import math

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    if math.sqrt(n) == int(math.sqrt(n)):
        print(1)
    else:
        print(0)
"""

import sys
import math

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    root = math.isqrt(n)
    print(1 if root * root == n else 0)

