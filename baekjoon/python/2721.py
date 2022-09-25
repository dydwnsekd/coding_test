import sys

triangular_number = [1]
for i in range(1, 302):
    triangular_number.append(triangular_number[i-1] + i)

n = int(sys.stdin.readline())

for _ in range(n):
    tn = int(sys.stdin.readline())
    result = 0
    for i in range(1, tn+1):
        print(i, triangular_number[i+1])
        result += i * triangular_number[i+1]
    print(result)
