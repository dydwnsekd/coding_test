"""
import sys

troom, tcond = map(int, sys.stdin.readline().strip().split())
mode = sys.stdin.readline().strip()

if mode == "freeze":
    if troom < tcond:
        print(troom)
    else:
        print(tcond)
elif mode == "heat":
    if troom > tcond:
        print(troom)
    else:
        print(tcond)
elif mode == "auto":
    print(tcond)
elif mode == "fan":
    print(troom)
"""

import sys

troom, tcond = map(int, sys.stdin.readline().split())
mode = sys.stdin.readline().rstrip('\n')

if mode == "freeze":
    print(min(troom, tcond))
elif mode == "heat":
    print(max(troom, tcond))
elif mode == "auto":
    print(tcond)
else:
    print(troom)

