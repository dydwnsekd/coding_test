import sys

a, b, c = map(int, sys.stdin.readline().strip().split())

if a + b == c:
    print("correct!")
else:
    print("wrong!")
