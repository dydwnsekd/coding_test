import sys

n = sys.stdin.readline().strip()
first_len = len(n)
count = 0

while True:
    n = str(int(n) * 2)
    if first_len < len(n):
        break

    count += 1

print(count)

