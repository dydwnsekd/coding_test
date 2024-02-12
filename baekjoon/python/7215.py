import sys

result = 0
n, k = map(int, sys.stdin.readline().strip().split())

socks_list = list(map(int, sys.stdin.readline().strip().split()))

if max(socks_list) < n:
    print(-1)
else:
    socks_list.sort()

    for i in socks_list:
        if i >= n:
            result += n - 1
        else:
            result += i

    print(result + 1)

