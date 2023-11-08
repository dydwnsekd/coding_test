import sys

def print_head(n):
    print("@" + "@" * n + "@")

def print_body(n):
    for i in range(n):
        print("@" + " " * n + "@")

n = int(sys.stdin.readline())

print_head(n)
print_body(n)
print_head(n)

