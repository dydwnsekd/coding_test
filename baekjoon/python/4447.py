import sys

n = int(sys.stdin.readline())

for _ in range(n):
    s = sys.stdin.readline().strip()
    if s.count("b") < s.count("g"):
        print(f"{s} is GOOD")
    elif s.count("b") == s.count("g"):
        print(f"{s} is NEUTRAL")
    else:
        print(f"{s} is BADDY")
