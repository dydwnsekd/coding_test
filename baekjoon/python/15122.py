import sys

n = int(sys.stdin.readline())

while True:
    n += 1

    if "0" not in str(n):
        break

print(n)

