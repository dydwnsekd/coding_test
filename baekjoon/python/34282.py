import sys

x, y, z = map(int, sys.stdin.readline().strip().split())
result = x * 0.25 + y * 0.25 + z * 0.5

if result >= 90:
    print("A")
elif result >= 80:
    print("B")
elif result >= 70:
    print("C")
elif result >= 60:
    print("D")
else:
    print("F")
