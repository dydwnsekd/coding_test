import sys

while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break

    before_t = 0
    result = 0
    for i in range(n):
        s, t = list(map(int, sys.stdin.readline().split()))
        result += s * (t-before_t)
    print(result)
