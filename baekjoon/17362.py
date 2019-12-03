import sys

n = int(sys.stdin.readline())
n = (n%8)

if n == 1:
    print (1)
elif n == 5:
    print (5)
elif n == 2 or n == 0:
    print (2)
elif n == 3 or n == 7:
    print (3)
else:
    print (4)