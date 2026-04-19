"""
import sys

L, R, A = map(int, sys.stdin.readline().strip().split())

diff = abs(L - R)

if A >= diff:
    A -= diff
    L = R = max(L, R)
    L += A // 2
    R += A // 2
else:
    if L < R:
        L += A
    else:
        R += A

print(min(L, R) * 2)
"""

import sys

L, R, A = map(int, sys.stdin.readline().split())

diff = abs(L - R)
use = min(A, diff)

A -= use

print((min(L, R) + use + A // 2) * 2)
