import sys

step = 0
n = sys.stdin.readline().strip()

while True:
    if len(n) == 1:
        break
    else:
        temp = 1
        for i in n:
            temp *= int(i)
        n = str(temp)
        step += 1

print(step)
