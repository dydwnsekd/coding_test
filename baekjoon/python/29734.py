import sys

n, m = map(int, sys.stdin.readline().strip().split())
t, s = map(int, sys.stdin.readline().strip().split())

dok = (m // 8) * (2 * t + s) + n
zip = ((n // 8) * s) + m

if dok < zip:
    print("Dok")
    print(dok)
else:
    print("Zip")
    print(zip)

