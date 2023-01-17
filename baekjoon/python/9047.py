# TODO
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    num = sys.stdin.readline().strip()
    count = 0
    while num != "6174":
        count += 1

        if len(num) < 4:
            while len(num) != 4:
                num += "0"

        max_str = ''.join(sorted(num, reverse=True))
        max_value = int(max_str)
        min_value = int(max_str[::-1])

        num = str(max_value - min_value)

    print(count)
