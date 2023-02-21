import sys

sys.stdin.readline()
problem_list = list(map(int,sys.stdin.readline().split()))

dp_list = [0 for _ in range(80001)]
dp_list[0] = 0

for i in range(1, 80001):
    dp_list[i] = dp_list[i-1]
    if i % 3 == 0 or i % 7 == 0:
        dp_list[i] += i
        

for i in problem_list:
    print(dp_list[i])
