"""
import sys

def print_head(n):
    for i in range(n):
        print("@" * 5 * n)

def print_body(n):
    for i in range(n):
        print("@" * n)

n = int(sys.stdin.readline())

print_head(n)
print_body(n)
print_head(n)
print_body(n)
print_body(n)
"""

import sys

n = int(sys.stdin.readline())

pattern = [5, 1, 5, 1, 1]

for p in pattern:
    for _ in range(n):
        print("@" * (p * n))

