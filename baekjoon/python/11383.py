import sys

n, m = map(int, sys.stdin.readline().strip().split())

for _ in range(n):
    s = sys.stdin.readline().strip()
    ss = sys.stdin.readline().strip()

    result = ""

    for i in s:
        result += f"{i}{i}"

    if result == ss:
        print("Eyfa")
    else:
        print("Not Eyfa")

