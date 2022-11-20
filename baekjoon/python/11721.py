import sys

s = sys.stdin.readline().strip()

i = len(s) // 10

for j in range(i+1):
    start_index = j*10
    end_index = (j+1) * 10
    print(s[start_index:end_index])
