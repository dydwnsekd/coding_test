import sys

n = int(sys.stdin.readline())

for _ in range(n):
    digit = sys.stdin.readline().strip()
    if digit[len(digit)//2] == digit[len(digit)//2 - 1]:
        print("Do-it")
    else:
        print("Do-it-Not")
