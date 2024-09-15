import sys

odd_number_list = []

for _ in range(7):
    n = int(sys.stdin.readline())

    if n % 2 == 1:
        odd_number_list.append(n)

if len(odd_number_list) == 0:
    print(-1)
else:
    print(sum(odd_number_list))
    print(min(odd_number_list))
