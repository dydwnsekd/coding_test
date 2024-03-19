import sys

result = 1
result_list = [0] * 10
for _ in range(3):
    result *= int(sys.stdin.readline())

result = str(result)

for s in result:
    result_list[int(s)] += 1

for i in range(0, 10):
    print(result_list[i])

