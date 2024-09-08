import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

if len(a) >= len(b):
    print("go")
else:
    print("no")

