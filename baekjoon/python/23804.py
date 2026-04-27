"""
import sys

def print_head(n):
    for i in range(n):
        print("@" * n * 5)

def print_body(n):
    for i in range(3 * n):
        print("@" * n)

n = int(sys.stdin.readline())

print_head(n)
print_body(n)
print_head(n)
"""

import sys

n = int(sys.stdin.readline())

pattern = [
    (5, n),      # head
    (1, 3 * n),  # body
    (5, n)       # head
]

for width_mul, height in pattern:
    line = "@" * (width_mul * n)
    for _ in range(height):
        print(line)
