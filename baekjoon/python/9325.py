import sys

n = int(sys.stdin.readline())

for _ in range(n):
    result = int(sys.stdin.readline())
    option_count = int(sys.stdin.readline())

    for _ in range(option_count):
        c, v = map(int, sys.stdin.readline().split())
        result += c*v

    print(result)
