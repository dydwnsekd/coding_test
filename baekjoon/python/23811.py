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
print_head(n)
"""

import sys

def print_block(width, height):
    for _ in range(height):
        print("@" * width)

n = int(sys.stdin.readline())

print_block(5 * n, n)
print_block(n, n)
print_block(5 * n, n)
print_block(n, n)
print_block(5 * n, n)
