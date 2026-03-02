"""
import sys

n = int(sys.stdin.readline())
s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

if s1 == s2:
    print("Good")
elif s1.count('w') == s2.count('w'):
    print("Its fine")
elif s1.count('w') > s2.count('w'):
    print("Oryang")
elif s1.count('w') < s2.count('w'):
    print("Manners maketh man")
"""

import sys

_ = sys.stdin.readline()
s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

if s1 == s2:
    print("Good")
else:
    c1, c2 = s1.count('w'), s2.count('w')
    print("Its fine" if c1 == c2 else ("Oryang" if c1 > c2 else "Manners maketh man"))

