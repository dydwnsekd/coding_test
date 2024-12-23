import sys

def get_factorial_num(num):
    if num == 1:
        return 1
    else:
        return num * get_factorial_num(num - 1)

n, k = map(int, sys.stdin.readline().strip().split())

print(int(get_factorial_num(n) / (get_factorial_num(k) * (get_factorial_num(n - k)))))
