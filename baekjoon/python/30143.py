"""
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, a, d = map(int, sys.stdin.readline().split())

    result = a

    for i in range(1, n):
        a += d
        result += a

    print(result)
"""

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, a, d = map(int, sys.stdin.readline().split())
    result = n * (2 * a + (n - 1) * d) // 2
    print(result)
