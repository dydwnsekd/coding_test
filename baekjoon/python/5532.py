import sys, math

L = int(sys.stdin.readline())
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())

day_1 = math.ceil(A/C)
day_2 = math.ceil(B/D)

if day_1 < day_2:
    print (L-day_2)
else:
    print (L-day_1)