import sys


a, b = sys.stdin.readline().strip().split()

a = sum(map(int, list(a)))
b = sum(map(int, list(b)))

print(a*b)
