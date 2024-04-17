import sys

t = int(sys.stdin.readline())

for _ in range(t):
    s = sys.stdin.readline().strip()
    if len(s) % 2 == 0:
        print(s[::2])
        print(s[1::2])
    else:
        print(s[::2] + s[1::2])
        print(s[1::2] + s[::2])
