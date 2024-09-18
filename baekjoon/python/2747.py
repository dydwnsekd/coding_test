import sys

def get_fibonacci_num(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return get_fibonacci_num(num - 1) + get_fibonacci_num(num - 2)

print(get_fibonacci_num(int(sys.stdin.readline().strip())))
