import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    card_list = []
    for _ in range(n):
        card_list.append(sys.stdin.readline().strip())

    if n % 2 == 0:
        a = card_list[:n//2]
        b = card_list[n//2:]
        for i in range(n // 2):
            print(a[i])
            print(b[i])
    else:
        a = card_list[:(n//2)+1]
        b = card_list[(n//2)+1:]
        for i in range(n // 2):
            print(a[i])
            print(b[i])
        print(a[-1])
