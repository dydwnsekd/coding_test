"""
import sys

d = float(sys.stdin.readline())
w = float(sys.stdin.readline())
n = int(sys.stdin.readline())

if w * n <= d * 3.141592:
    print("YES")
else:
    print("NO")
"""

import sys
import math

def can_wrap(diameter: float, width: float, count: int) -> bool:
    return width * count <= diameter * math.pi

if __name__ == "__main__":
    d = float(sys.stdin.readline().strip())
    w = float(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())

    print("YES" if can_wrap(d, w, n) else "NO")

