import sys

cases = int(sys.stdin.readline())
value_list = [50, 20, 10, 5, 1]

for _ in range(cases):
    a, b = map(float, sys.stdin.readline().split())
    remain_count = []
    remain_value = b - a

    for i in value_list:
        remain_value = remain_value % i
        remain_count.append(remain_value//i)

    for i in range(len(value_list)):
        print(f"{remain_count[i]}-${value_list[i]}", end=", ")

