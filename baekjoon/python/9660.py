import sys

n = int(sys.stdin.readline())

if n % 7 == 0 or n % 7 == 2:
    print("CY")
else:
    print("SK")
