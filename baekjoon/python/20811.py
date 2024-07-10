import sys


def get_fibonacci_num(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return get_fibonacci_num(num - 1) + get_fibonacci_num(num - 2)


n = int(sys.stdin.readline())

i = 1
count = 0

while True:
    if count + get_fibonacci_num(i) >= n:
        break
    else:
        count += get_fibonacci_num(i)
        i += 1

print(i)

