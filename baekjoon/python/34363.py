import sys

FEET_TO_MILE = 5280

s = int(sys.stdin.readline())
d = float(sys.stdin.readline())
t = float(sys.stdin.readline())

s_feet = s * FEET_TO_MILE / 3600

if (t * s_feet) >= d:
    print("MADE IT")
else:
    print("FAILED TEST")

