import sys

count = 0
n = int(sys.stdin.readline())

for i in range(1, 500):
    for j in range(i, 500):
        if j ** 2 - i ** 2 == n:
            count += 1

print(count)
