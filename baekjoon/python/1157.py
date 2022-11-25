import sys

alpha_dict = {}
for i in range(65, 91):
    alpha_dict[chr(i)] = 0

s = sys.stdin.readline().strip().upper()

for i in s:
    alpha_dict[i] = alpha_dict[i] + 1


