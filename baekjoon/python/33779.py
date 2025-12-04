import sys

s = sys.stdin.readline().strip()

if s == s[::-1]:
    print("beep")
else:
    print("boop")
