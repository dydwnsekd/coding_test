import sys

count = 0
n = int(sys.stdin.readline())

for i in range(n):
    if sys.stdin.readline().strip().startswith('C'):
        count += 1

print(count)
