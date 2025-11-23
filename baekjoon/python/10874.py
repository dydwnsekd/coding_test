import sys

n = int(sys.stdin.readline())
result = []

for i in range(n):
    answer_list = list(map(int, sys.stdin.readline().strip().split()))

    flag = True
    for j in range(10):
        if answer_list[j] != (j % 5) + 1:
            flag = False
            break

    if flag:
        result.append(i + 1)

print('\n'.join(map(str, result)))
