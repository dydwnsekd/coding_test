import sys


def get_fibonacci_list(num):
    fibonacci_list = [0, 1, 1]

    for i in range(3, num+1):
        fibonacci_list.append(fibonacci_list[i-2] + fibonacci_list[i-1])

    return fibonacci_list

n, m = list(map(int, sys.stdin.readline().split()))
fibonacci_list = get_fibonacci_list(m)

for i in range(n, m+1):
    print(fibonacci_list[i] % 10, end="")
