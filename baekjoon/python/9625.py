import sys

n = int(sys.stdin.readline())

A_count = 1
B_count = 0

for i in range(n):
    a = A_count
    b = B_count

    A_count = b
    B_count = a + b

print(f"{A_count} {B_count}")
