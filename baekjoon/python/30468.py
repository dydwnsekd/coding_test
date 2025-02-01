import sys

str, dex, int, luk, n = map(int, sys.stdin.readline().strip().split())

if (str + dex + int + luk) >= n * 4:
    print(0)
else:
    print((n * 4) - str - dex - int - luk)
