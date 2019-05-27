import sys

end_num = int(1000 ** 0.5)

sosu_list = [True for i in range(1001)]
sosu_list[0] = False
sosu_list[1] = False

for i in range(2, end_num+1):

    if sosu_list[i] == True:
        for j in range(i+i, 1001, i):
            sosu_list[j] = False

num_count = int(sys.stdin.readline())
problem_list = sys.stdin.readline().split(" ")

count = 0

for i in problem_list:
    if sosu_list[int(i)] == True:
        count += 1

print (count)
