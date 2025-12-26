import sys

d = float(sys.stdin.readline())
w = float(sys.stdin.readline())
n = int(sys.stdin.readline())

if w * n <= d * 3.141592:
    print("YES")
else:
    print("NO")
