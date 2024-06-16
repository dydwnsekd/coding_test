import sys

n = int(sys.stdin.readline())

for _ in range(n):
    num = int(sys.stdin.readline())
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
