"""
import sys

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    if n <= 1000000:
        print(n)
    elif n <= 5000000:
        print(int(n - n * 0.1))
    else:
        print(int(n - n * 0.2))
"""

import sys

while True:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break

    if n <= 1_000_000:
        discount = 0
    elif n <= 5_000_000:
        discount = 0.1
    else:
        discount = 0.2

    final_price = int(n * (1 - discount))
    print(final_price)

