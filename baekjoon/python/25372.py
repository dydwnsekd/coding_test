import sys

n = int(sys.stdin.readline())

for _ in range(n):
    s = sys.stdin.readline().strip()
    if 6 <= len(s) <= 9:
        print("yes")
    else:
        print("no")
