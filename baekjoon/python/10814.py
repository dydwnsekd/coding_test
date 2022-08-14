import sys

n = int(sys.stdin.readline())
user_list = []
for _ in range(n):
    user_list.append(list(sys.stdin.readline().split()))

user_list = sorted(user_list, key=lambda user_list: [user_list[0], user_list[1]])

for age, name in user_list:
    print(age, name)
