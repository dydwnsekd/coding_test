c = 0
temp = 1
num = int(input())

while temp < num:
    temp += 6 * c
    c += 1

if num == 1:
    print(1)
else:
    print(c)
