import sys

n = int(sys.stdin.readline())
count_0 = 0
count_1 = 0

for _ in range(n):
    temp = int(sys.stdin.readline())
    if temp == 0:
        count_0 += 1
    else:
        count_1 += 1

if count_0 > count_1:
    print ("Junhee is not cute!")
else:
    print ("Junhee is cute!")