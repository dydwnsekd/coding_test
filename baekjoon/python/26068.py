import sys

count = 0
n = int(sys.stdin.readline())

for _ in range(n):
    if 90 >= int(sys.stdin.readline().strip().split("-")[1]):
        count += 1

print(count)
