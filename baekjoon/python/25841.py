import sys

count = 0
start_num, end_num, digit_num = map(int, sys.stdin.readline().split())
digit_num = str(digit_num)

for i in range(start_num, end_num+1):
    for j in str(i):
        if digit_num == j:
            count += 1

print(count)

