import sys

n, m = list(map(int, (sys.stdin.readline().split())))

if m <= 2:
    print("NEWBIE!")
elif m <= n:
    print("OLDBIE!")
else:
    print("TLE!")
