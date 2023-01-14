# TODO
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    num = sys.stdin.readline().strip()
    count = 0
    while True:
        if num == "6174":
            break

        count += 1
        max_value = int(''.join(sorted(num, reverse=True)))
        min_value = int(''.join(sorted(num)))

        num = str(max_value - min_value)

    print(count)
