import sys

def get_factorial_num(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

n, k = map(int, sys.stdin.readline().strip().split())

print(int(get_factorial_num(n) / (get_factorial_num(k) * (get_factorial_num(n - k)))))
