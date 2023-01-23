import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    card_list = []
    for _ in range(n):
        card_list.append(sys.stdin.readline().split())

    if n % 2 == 0:
        for i in range(0, n, 2):
            print(card_list[i])
        for i in range(1, n, 2):
            print(card_list[i])

    else:
        print(card_list[0])
        for i in range(1, n, 2):
            print(card_list[i])
        for i in range(2, n, 2):
            print(card_list[i])

