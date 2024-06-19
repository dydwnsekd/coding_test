import sys

acres = 4840
w, h = map(int, sys.stdin.readline().strip().split())

print(((w*h) // (acres * 5)) + 1)
