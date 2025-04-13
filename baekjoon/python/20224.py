import sys

while True:
    count = 0
    n = int(sys.stdin.readline())

    if n == 0:
        break

    num_list = sys.stdin.readline().split()

    for i in range(n-3):
        if '2020' == ''.join(num_list[i:i+4]):
            count += 1

    print(count)


