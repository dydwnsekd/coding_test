import sys

n = sys.stdin.readline().strip()
count = 0
first_num = n
last_num = 0
temp = 0

while True:
    count += 1
    if int(n) < 10:
        n = "0" + str(n)

    t1 = int(n[-1])
    t2 = sum(list(map(int, n))) % 10
    last_num = str(int(str(t1) + str(t2)))

    if first_num == last_num:
        print(count)
        break
    n = str(last_num)
