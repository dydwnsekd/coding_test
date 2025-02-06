import sys

n = int(sys.stdin.readline())

a, b = map(int, sys.stdin.readline().split())
drink_count = a // 2 + b

print(min(n, drink_count))
