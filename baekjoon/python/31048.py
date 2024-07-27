import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    if n >= 5:
        print(0)
    else:
        answer = 1
        for i in range(1, n+1):
            answer *= i
        print(answer % 10)
