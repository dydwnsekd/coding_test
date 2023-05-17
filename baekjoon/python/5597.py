import sys

student_list = [0] * 30

for _ in range(28):
    n = int(sys.stdin.readline())
    student_list[n-1] = 1

for i in range(30):
    if student_list[i] == 0:
        print(i+1)
