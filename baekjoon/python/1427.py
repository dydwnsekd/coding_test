import sys

n = list(sys.stdin.readline().rstrip())

n.sort()
n.reverse()

for i in n:
    print(i, end="")