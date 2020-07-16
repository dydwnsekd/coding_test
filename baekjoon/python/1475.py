import sys
import math

num = sys.stdin.readline().replace("\n", "")
num_count = [0.0 for i in range(9)]

for i in range(len(num)):
    if num[i] == '6' or num[i] == '9':
        num_count[6] += 0.5
    else:
        num_count[int(num[i])] += 1

print (math.ceil(max(num_count)))
