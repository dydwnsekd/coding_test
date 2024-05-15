import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = sys.stdin.readline().split()
    s = sys.stdin.readline().split()

    if m == "C":
        for i in s:
            print(ord(i) - 64, end=" ")
        print()
    else:
        for i in s:
            print(chr(int(i) + 64), end=" ")
        print()

