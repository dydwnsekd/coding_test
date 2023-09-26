import sys, math

n, w, h = list(map(int, sys.stdin.readline().split()))
max_value = math.sqrt(w**2 + h**2)

for _ in range(n):
    if int(sys.stdin.readline()) <= max_value:
        print("DA")
    else:
        print("NE")

