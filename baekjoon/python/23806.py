# 골뱅이 찍기 - ㅁ
"""
import sys

def print_head(n):
    for i in range(n):
        print("@" * n * 5)

def print_body(n):
    for i in range(3 * n):
        print("@" * n + " " * 3 * n + "@" * n)

n = int(sys.stdin.readline())

print_head(n)
print_body(n)
print_head(n)
"""

import sys

n = int(sys.stdin.readline())

head = "@" * (5 * n)
body = "@" * n + " " * (3 * n) + "@" * n

pattern = [
    (head, n),
    (body, 3 * n),
    (head, n),
]

for line, count in pattern:
    for _ in range(count):
        print(line)
