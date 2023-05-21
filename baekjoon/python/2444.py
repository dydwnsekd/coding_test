import sys

n = int(sys.stdin.readline())

for i in range(n):
    space = " " * (n-i-1)
    star = "*" * (2*i+1)
    print(space+star)

for i in range(n-2, -1, -1):
    space = " " * (n-i-1)
    star = "*" * (2*i+1)
    print(space+star)
