import sys

ax, ay, az = map(int, sys.stdin.readline().split())
bx, by, bz = map(int, sys.stdin.readline().split())

print(bx-az, by//ay, bz-ax)
