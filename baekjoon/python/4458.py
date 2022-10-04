import sys

n = int(sys.stdin.readline())

for _ in range(n):
    str = sys.stdin.readline()
    print(str[0].upper() + str[1:])
