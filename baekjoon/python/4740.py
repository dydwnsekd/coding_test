import sys

while True:
    s = sys.stdin.readline().replace("\n", "")

    if s == "***":
        break

    else:
        print(s[::-1])
