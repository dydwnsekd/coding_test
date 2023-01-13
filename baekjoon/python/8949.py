import sys

n1, n2 = sys.stdin.readline().split()
result = ""
len_n1 = len(n1)
len_n2 = len(n2)

long_len = max(len_n1, len_n2)

if len_n1 < long_len:
    temp = "0" * (long_len-len_n1)
    n1 = temp + n1

if len_n2 < long_len:
    temp = "0" * (long_len-len_n2)
    n2 = temp + n2

for i in range(long_len):
    result += str(int(n1[i]) + int(n2[i]))

print(result)
