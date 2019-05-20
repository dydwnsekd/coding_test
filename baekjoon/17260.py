import sys

problem_count = int(sys.stdin.readline().split()[0])

problem_list = sys.stdin.readline().split()

for i in range(problem_count):
    cur = int(problem_list[i])

    result = 0

    for j in range(cur+1):
        if j % 3 == 0 or j % 7 ==0:
            result += j

    print (result)