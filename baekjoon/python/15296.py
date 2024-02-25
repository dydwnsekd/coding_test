import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    num_list = []
    k, b, n = map(int, sys.stdin.readline().strip().split())

    while n > b:
        num_list.append(n % b)
        n = n // b

    num_list.append(n)
    result = 0

    for i in num_list:
        result += i**2

    print(k, result)

