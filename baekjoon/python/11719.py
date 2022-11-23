import sys

while True:
    s = sys.stdin.readline().replace("\n", "")
    if len(s) != 0:
        print(s)
    else:
        break
