import sys

def print_head(n):
    for i in range(4*n):
        print("@" * n)

def print_body(n):
    for i in range(n):
        print("@" * n * 5)

n = int(sys.stdin.readline())

print_head(n)
print_body(n)

