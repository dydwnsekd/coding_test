import sys

n = int(sys.stdin.readline())

if n % 4 == 1:
    print("Either")
elif n % 4 == 2:
    print("Odd")
elif n % 4 == 3:
    print("Either")
elif n % 4 == 0:
    print("Even")

