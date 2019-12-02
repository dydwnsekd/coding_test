import sys

n = int(sys.stdin.readline())
n = (n%8)

if n == 6:
    print (4)
elif n == 7:
    print (3)
elif n == 8:
    print (2)
else:
    print (n)