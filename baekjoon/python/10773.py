import sys

result = list()

n = int(sys.stdin.readline())

for _ in range(n):
    temp_num = int(sys.stdin.readline())
    if temp_num == 0:
        result.pop()
    else:
        result.append(temp_num)

print (sum(result))