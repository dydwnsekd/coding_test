import sys

odd_number_list = []

for _ in range(7):
    n = int(sys.stdin.readline())

    if n % 2 == 1:
        odd_number_list.append(n)

print(sum(odd_number_list))
print(min(odd_number_list))
