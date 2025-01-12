import sys

n = int(sys.stdin.readline())

for _ in range(n):
    num = sys.stdin.readline().strip()

    if (int(num[:2]) ** 2 + int(num[2:]) ** 2) % 7 == 1:
        print("YES")
    else:
        print("NO")
