import sys

person_count = int(sys.stdin.readline())
time_list = list(map(int, sys.stdin.readline().split(" ")))

time_list.sort()

for i in range(1, len(time_list)):
    time_list[i] = time_list[i-1] + time_list[i]

result = sum(time_list)

print(result)