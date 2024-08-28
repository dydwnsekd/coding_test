import sys

while True:
    s = sys.stdin.readline().strip()

    if s == "END":
        break

    print(s[::-1])
