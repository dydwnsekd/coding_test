# TODO 좀 더 효율적으로 할 수 없을까?
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    s = sys.stdin.readline().strip()
    result = s

    for i in range(len(s)):
        temp_s = s[i:] + s[:i]

        if result > temp_s:
            result = temp_s

    print(result)
