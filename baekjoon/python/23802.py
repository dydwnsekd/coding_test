import sys

def print_head(n):
    for i in range(n):
        print("@" * n * 5)

def print_body(n):
    for i in range(4*n):
        print("@" * n)


n = int(sys.stdin.readline())

print_head(n)
print_body(n)

