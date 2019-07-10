import sys

A, B = list(map(int, sys.stdin.readline().split(" ")))

if A > B:
    print (">")
elif A==B:
    print ("==")
else:
    print ("<")
