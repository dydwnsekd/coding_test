import sys

cases = int(sys.stdin.readline())
value_list = [50, 20, 10, 5, 1]

for _ in range(cases):
    a, b = map(float, sys.stdin.readline().split())
    remain_count = []
    combine_text = []
    remain_value = b - a

    for i in value_list:
        remain_count.append(int(remain_value//i))
        remain_value = remain_value % i

    for i in range(len(value_list)):
        combine_text.append(f"{remain_count[i]}-${value_list[i]}")

    print(", ".join(combine_text))

