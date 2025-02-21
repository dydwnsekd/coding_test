import sys

count = 0

n = int(sys.stdin.readline())
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

for i in range(n):
    if i % a != 0 and i % b == 0:
        count += 1
    elif i % a == 0 and i % b != 0:
        count += 1

print(count)
