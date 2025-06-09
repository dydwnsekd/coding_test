# commit 대기
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

