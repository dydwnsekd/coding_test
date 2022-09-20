import sys

n = int(sys.stdin.readline())
for _ in range(n):
    m = int(sys.stdin.readline())
    answer = 0
    store_list = list(map(int, sys.stdin.readline().split()))

    avg = sum(store_list) // m
    for i in store_list:
        answer += abs(avg - i)
    print(answer)