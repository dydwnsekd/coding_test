"""
import sys

a, b, c, d = map(int, sys.stdin.readline().strip().split())

if a + b <= d and c <= d:
    print("~.~")
elif a + b > d and c > d:
    print("T.T")
elif a + b <= d and c > d:
    print("Shuttle")
elif a + b > d and c <= d:
    print("Walk")
"""
"""
import sys

a, b, c, d = map(int, sys.stdin.readline().strip().split())

if (a + b <= d) == (c <= d):
    print("~.~" if a + b <= d else "T.T")
else:
    print("Shuttle" if a + b <= d else "Walk")
"""

import sys

a, b, c, d = map(int, sys.stdin.readline().strip().split())

ab_ok = (a + b) <= d
c_ok = c <= d

RESULT = {
    (True,  True):  "~.~",
    (False, False): "T.T",
    (True,  False): "Shuttle",
    (False, True):  "Walk",
}

print(RESULT[(ab_ok, c_ok)])
