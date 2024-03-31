import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    n = sys.stdin.readline().strip()

    if (int(n) + 1) % int(n[2:]) == 0:
        print("Good")
    else:
        print("Bye")
