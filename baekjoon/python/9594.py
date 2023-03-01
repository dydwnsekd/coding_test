# TODO https://vsfe.tistory.com/24
import sys

while True:
    n = int(sys.stdin.readline())
    even_zero = True
    count = 1
    last_num = 1
    if n == -1:
        break

    for i in range(1, n+1):
        last_num *= i
        # print(i, last_num)

        if last_num % 10 == 0:
            even_zero = not even_zero
        last_num = last_num // 10
        if even_zero:
            count += 1

    print(count)
