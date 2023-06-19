import sys

cases = int(sys.stdin.readline())

student_list = list(map(int, sys.stdin.readline().split()))
temp_list = []

for i in student_list:
    if student_list.count(i) == 1:
        print(i)
        break
