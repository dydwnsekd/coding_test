import sys

s = "SciComLove"
n = int(sys.stdin.readline())

if n % 2 == 0:
    print(s)
else:
    print(s[::-1])
