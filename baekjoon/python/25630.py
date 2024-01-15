import sys

count = 0

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

if n % 2 == 1:
    a = s[:n // 2]
    b = s[n // 2 + 1:]

    for i in range(n//2):
        if a[i] != b[i]:
            count += 1

else:
    a = s[:n // 2]
    b = s[n // 2:]

    print(a)
    print(b)

    for i in range(n//2):
        if a[i] != b[i]:
            count += 1

print(count)
