import sys

w, h = map(float, sys.stdin.readline().strip().split())

print(round(w * h * 0.5, 1))
