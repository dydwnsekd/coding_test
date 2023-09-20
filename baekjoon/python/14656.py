import sys

result = 0

n = int(sys.stdin.readline())
student_list = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    if i+1 != student_list[i]:
        result += 1

print(result)
