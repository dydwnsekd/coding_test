import sys

while True:
    n, m = map(int, sys.stdin.readline().split())
    result = 0

    if n == 0 and m == 0:
        break

    human_list = list(map(int, sys.stdin.readline().split()))
    avg_value = m // n
    for i in human_list:
        if i < avg_value:
            result += i
        else:
            result += avg_value

    print(result)
