import sys
sys.setrecursionlimit(10**7)

def factorial(num):
    if num > 1:
        return (num * factorial(num-1)) % 10
    elif num <= 1:
        return 1

n = int(sys.stdin.readline())
result = factorial(n)
print(result % 10)
