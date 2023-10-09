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
        break
    elif n < s:
        s = 1

print(seconds)
