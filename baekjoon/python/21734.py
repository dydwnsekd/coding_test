import sys

s = sys.stdin.readline().strip()

for i in s:
    i_num = 0
    for n in str(ord(i)):
        i_num += int(n)

    print(i * i_num)
