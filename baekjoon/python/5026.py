import sys

n = int(sys.stdin.readline())

for _ in range(n):
    p = sys.stdin.readline()
    if "=" in p:
        print("skipped")
    elif "+" in p:
        print(int(p.split("+")[0]) + int(p.split("+")[1]))
