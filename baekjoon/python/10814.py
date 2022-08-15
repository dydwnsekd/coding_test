import sys

n = int(sys.stdin.readline())
user_list = []
for i in range(n):
    user_list.append([list(sys.stdin.readline().split()), i])

user_list = sorted(user_list, key=lambda user_list: [int(user_list[0][0]), user_list[1]])

for user_info in user_list:
    print(user_info[0][0], user_info[0][1])
