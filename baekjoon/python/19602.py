import sys

s = int(sys.stdin.readline())
m = int(sys.stdin.readline())
l = int(sys.stdin.readline())

if s + m * 2 + l * 3 >= 10:
    print("happy")
else:
    print("sad")

