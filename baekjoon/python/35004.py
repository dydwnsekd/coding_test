"""
import sys

count = 0

n = int(sys.stdin.readline())
bin_n = bin(n)

while int(bin_n, 2) != 0:
    reverse_n = '0b' + bin_n[2:][::-1]
    bin_n = bin(int(reverse_n, 2) - 1)

    count += 1

print(count)
"""

import sys

def reverse_bits(x: int) -> int:
    rev = 0
    while x > 0:
        rev = (rev << 1) | (x & 1)
        x >>= 1
    return rev

n = int(sys.stdin.readline().strip())
count = 0

while n > 0:
    n = reverse_bits(n) - 1
    count += 1

print(count)

