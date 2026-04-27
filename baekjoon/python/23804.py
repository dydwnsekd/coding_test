# 골뱅이 찍기 - ㄷ

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

