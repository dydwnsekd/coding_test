import sys

result_list = [0 for _ in range(11)]
result_list[0] = 0
result_list[1] = 1
result_list[2] = 2
result_list[3] = 4

for i in range(4,11):
    result_list[i] = result_list[i-3] + result_list[i-2] + result_list[i-1]

problem_count = int(sys.stdin.readline().split()[0])

for _ in range(problem_count):
    i = int(sys.stdin.readline().split()[0])

    print(result_list[i])