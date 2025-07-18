import sys

count = 0
n, m = map(int, sys.stdin.readline().strip().split())

for _ in range(n):
    m = sys.stdin.readline().strip()

    if m.count('O') > m.count('X'):
        count += 1

print(count)
