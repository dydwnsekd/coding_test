import sys

n = sys.stdin.readline().strip()

while True:
    digits_sum = 0

    for i in n:
        digits_sum += int(i)

    if int(n) % digits_sum == 0:
        break

    n = str(int(n) + 1)

print(n)

