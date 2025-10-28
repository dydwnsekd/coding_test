import sys

mile_to_feet = 5280

w = int(sys.stdin.readline())
n = int(sys.stdin.readline())

print((w * mile_to_feet) // n)
