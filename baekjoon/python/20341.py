import sys

result = []
days = int(sys.stdin.readline())

a_distance = list(map(int, sys.stdin.readline().strip().split()))
b_distance = list(map(int, sys.stdin.readline().strip().split()))
c_distance = list(map(int, sys.stdin.readline().strip().split()))

for i in range(days):
    temp_list = [a_distance[i], b_distance[i], c_distance[i]]
    temp_list.sort()

    result.append(temp_list[1])

print(*result)
