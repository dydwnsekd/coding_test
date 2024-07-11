import sys

n = int(sys.stdin.readline())

for i in range(n):
    l = int(sys.stdin.readline())
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()

    count = 0
    for j in range(l):
        if a[j] != b[j]:
            count += 1

    print(f"Case {i+1}: {count}")

