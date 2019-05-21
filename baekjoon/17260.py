import sys

sys.stdin.readline()
problem_list = list(map(int,sys.stdin.readline().split()))

for i in problem_list:
    result = 0

    count3 = int(i/3)
    count7 = int(i/7)

    for j in range(1, count3+1):
        result += j*3

    for j in range(1, count7+1):
        if (j*7) % 3 != 0:
            result += j*7

    print (result)