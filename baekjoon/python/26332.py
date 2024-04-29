import sys

n = int(sys.stdin.readline())

for _ in range(n):
    count, value = map(int, sys.stdin.readline().split())
    result = count * value

    print(count, value)
    if count > 1:
        print(result - (count-1) * 2)
    else:
        print(result)
