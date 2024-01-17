import sys

s = sys.stdin.readline().strip()

if len(s) == len(set(s)):
    print(1)
else:
    print(0)
