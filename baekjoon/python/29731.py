import sys

n = int(sys.stdin.readline())
flag = True

str_list = [
    "Never gonna give you up",
    "Never gonna let you down",
    "Never gonna run around and desert you",
    "Never gonna make you cry",
    "Never gonna say goodbye",
    "Never gonna tell a lie and hurt you",
    "Never gonna stop",
]

for i in range(n):
    s = sys.stdin.readline().strip()

    if s not in str_list:
        flag = False
        break

if flag:
    print("No")
else:
    print("Yes")
