import sys

num = sys.stdin.readline().split()[0]
digit_num = len(num)
split_num = int(sys.stdin.readline())

start_num = int(num) - int(num[-2:])
end_num = start_num + 100

answer = 0

for i in range(start_num, end_num):
    if i % split_num == 0:
        answer = str(i)[-2:]
        break

print (answer)