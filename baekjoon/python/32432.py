import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

if n == 1:
    print(k)
else:
    k = k - n
    print(k // n)

