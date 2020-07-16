import sys

n = int(sys.stdin.readline())

while True:
    num = int(sys.stdin.readline())
    if num == 0:
        break
    elif num % n != 0:
        print("%d is NOT a multiple of %d." % (num, n))
    else:
        print("%d is a multiple of %d." % (num, n))