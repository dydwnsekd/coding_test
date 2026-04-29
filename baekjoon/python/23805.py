# 골뱅이 찍기 - 돌아간 ㄹ

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

