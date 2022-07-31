import sys

n = sys.stdin.readline()

for i in range(int(n)+1):
    temp = int(i)
    for j in str(i):
        temp += int(j)

    if temp == int(n):
        print(i)
        exit()

print(0)
