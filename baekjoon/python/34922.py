import sys

w, h = map(int, sys.stdin.readline().strip().split())
r = int(sys.stdin.readline())

print(round((w * h) - ((r ** 2) * 3.141592 / 4 ), 2))
