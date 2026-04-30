# 골뱅이 찍기 - 돌아간 ㄹ

"""
import sys

def print_head(n):
    for i in range(n):
        print("@"*n*3 + " "*n + "@"*n)

def print_body(n):
    for i in range(3*n):
        print("@"*n + " "*n + "@"*n + " "*n + "@"*n)

def print_tail(n):
    for i in range(n):
        print("@"*n + " "*n + "@"*n*3)

n = int(sys.stdin.readline())

print_head(n)
print_body(n)
print_tail(n)
"""

import sys

n = int(sys.stdin.readline())

head = "@" * (3 * n) + " " * n + "@" * n
body = "@" * n + " " * n + "@" * n + " " * n + "@" * n
tail = "@" * n + " " * n + "@" * (3 * n)

pattern = [
    (head, n),
    (body, 3 * n),
    (tail, n),
]

for line, count in pattern:
    for _ in range(count):
        print(line)
