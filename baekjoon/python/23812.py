import sys

def print_head(n):
    for i in range(n):
        print("@"*n + " "*3*n + "@"*n)

def print_body(n):
    for i in range(n):
        print("@" * 5 * n)

n = int(sys.stdin.readline())

print_head(n)
print_body(n)
print_head(n)
print_body(n)
print_head(n)
