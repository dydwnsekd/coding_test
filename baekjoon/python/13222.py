import sys
import math

n, w, h = list(map(int, sys.stdin.readline().split()))
max_length = math.sqrt(w**2 + h**2)

for _ in range(n):
    length = int(sys.stdin.readline())
    if length <= max_length:
        print("YES")
    else:
        print("NO")
