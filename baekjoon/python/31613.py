import sys

x = int(sys.stdin.readline())
n = int(sys.stdin.readline())

count = 0

while x < n:
    count += 1

    r = x % 3

    if r == 0:
        x = x + 1
    elif r == 1:
        x = x * 2
    elif r == 2:
        x = x * 3

print(count)

