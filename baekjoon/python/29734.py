import sys

n, m = map(int, sys.stdin.readline().strip().split())
t, s = map(int, sys.stdin.readline().strip().split())

if m % 8 == 0:
    dok_mok = (m // 8) - 1
else:
    dok_mok = m // 8
if n % 8 == 0:
    zip_mok = (n // 8) - 1
else:
    zip_mok = n // 8

dok = t + dok_mok * (2 * t + s) + m
zip = zip_mok * s + n

if dok < zip:
    print("Dok")
    print(dok)
else:
    print("Zip")
    print(zip)

