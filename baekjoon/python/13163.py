import sys

n = int(sys.stdin.readline())

for _ in range(n):
    s = sys.stdin.readline().strip().split()
    s[0] = "god"

    print("".join(s))
