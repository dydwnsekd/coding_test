import sys

count = 0
n = int(sys.stdin.readline())

for i in range(1, 1000):
    for j in range(i, 1000):
        if j ** 2 - i ** 2 == n:
            count += 1


print(count)
