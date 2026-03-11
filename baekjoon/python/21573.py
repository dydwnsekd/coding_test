import sys

troom, tcond = map(int, sys.stdin.readline().strip().split())
mode = sys.stdin.readline().strip()

if mode in ("freeze", "heat", "auto"):
    print(tcond)
else:
    print(troom)
