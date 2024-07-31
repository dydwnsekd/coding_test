import sys

sit_list = []
reject_count = 0

n = int(sys.stdin.readline())

person_list = list(map(int, sys.stdin.readline().strip().split()))

for i in person_list:
    if i in sit_list:
        reject_count += 1
    else:
        sit_list.append(i)

print(reject_count)
