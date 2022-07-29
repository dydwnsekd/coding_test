import sys
from itertools import combinations

answer = 9999999

n, m = list(map(int, sys.stdin.readline().split()))
num_list = list(map(int, sys.stdin.readline().split()))

sum_list = list(map(sum, list(combinations(num_list, 3))))

for i in sum_list:
    if (m >= i) and (m-i < abs(m-answer)):
        answer = i

print(answer)
