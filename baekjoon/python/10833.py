import sys

student_list = []
apple_list = []
result = 0
n = int(sys.stdin.readline())

for _ in range(n):
    s, a = map(int, sys.stdin.readline().split())
    student_list.append(s)
    apple_list.append(a)

for i in range(n):
    result += apple_list[i] % student_list[i]

print(result)
