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
        max_str = ''.join(sorted(num, reverse=True))
        max_value = int(max_str)
        min_value = int(max_str[::-1])

        num = str(max_value - min_value)

    print(count)
