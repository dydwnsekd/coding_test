import sys

n = int(sys.stdin.readline())
c = int(sys.stdin.readline())
p = int(sys.stdin.readline())

if c * p < n:
    print("no")
else:
    print("yes")

