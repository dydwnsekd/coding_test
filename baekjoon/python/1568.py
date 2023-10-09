import sys

s = 1
seconds = 0

n = int(sys.stdin.readline())

while True:
    if n > s:
        n -= s
        s += 1
        seconds += 1
    elif n == s:
        seconds += 1
        break
    elif n < s:
        s = 1

print(seconds)
