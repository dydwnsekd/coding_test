import sys

emp_list = []

n = int(sys.stdin.readline())

for i in range(n):
    temp_s = sys.stdin.readline().strip().replace("-", "").upper()
    if temp_s not in emp_list:
        emp_list.append(temp_s)

print(len(emp_list))
