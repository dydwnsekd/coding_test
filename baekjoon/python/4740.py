import sys

while True:
    s = sys.stdin.readline().strip()

    if s == "***":
        break

    else:
        print(s[::-1])
